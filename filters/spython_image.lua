-- Filtro pandoc que renderiza blocos de código com classe `python-image`
-- como uma imagem gerada pelo spython.
--
-- O conteúdo do bloco pode ter duas partes separadas por uma linha em branco:
-- a primeira é "hide" (incluída no script mas não exibida no slide),
-- a segunda é o conteúdo exibido, cuja primeira linha começa com `>>> `
-- (e linhas de continuação com `... `) e contém a expressão final que é
-- passada para `to_pdf`.
--
-- Imports do spython são adicionados automaticamente.

local cont = 0

-- usa o PID do processo para garantir unicidade entre builds paralelos
-- (slides + handout + tex frequentemente iniciam no mesmo segundo)
local function get_uuid()
    local p = io.popen("echo $$")
    if p then
        local pid = p:read("*a")
        p:close()
        if pid then return (pid:gsub("%s+", "")) end
    end
    math.randomseed(os.time())
    return string.format("%x%x", os.time(), math.random(0, 1000000000))
end
local UUID = get_uuid()

local IMPORTS = [[
from spython import (
    Color, rgb, rgba,
    aliceblue, antiquewhite, aqua, aquamarine, azure, beige, bisque, black,
    blanchedalmond, blue, blueviolet, brown, burlywood, cadetblue, chartreuse,
    chocolate, coral, cornflowerblue, cornsilk, crimson, cyan, darkblue,
    darkcyan, darkgoldenrod, darkgray, darkgreen, darkkhaki, darkmagenta,
    darkolivegreen, darkorange, darkorchid, darkred, darksalmon, darkseagreen,
    darkslateblue, darkslategray, darkturquoise, darkviolet, deeppink,
    deepskyblue, dimgray, dodgerblue, firebrick, floralwhite, forestgreen,
    fuchsia, gainsboro, ghostwhite, gold, goldenrod, gray, green, greenyellow,
    honeydew, hotpink, indianred, indigo, ivory, khaki, lavender, lavenderblush,
    lawngreen, lemonchiffon, lightblue, lightcoral, lightcyan,
    lightgoldenrodyellow, lightgray, lightgreen, lightpink, lightsalmon,
    lightseagreen, lightskyblue, lightslategray, lightsteelblue, lightyellow,
    lime, limegreen, linen, magenta, maroon, mediumaquamarine, mediumblue,
    mediumorchid, mediumpurple, mediumseagreen, mediumslateblue,
    mediumspringgreen, mediumturquoise, mediumvioletred, midnightblue,
    mintcream, mistyrose, moccasin, navajowhite, navy, oldlace, olive,
    olivedrab, orange, orangered, orchid, palegoldenrod, palegreen,
    paleturquoise, palevioletred, papayawhip, peachpuff, peru, pink, plum,
    powderblue, purple, red, rosybrown, royalblue, saddlebrown, salmon,
    sandybrown, seagreen, seashell, sienna, silver, skyblue, slateblue,
    slategray, snow, springgreen, steelblue, tan, teal, thistle, tomato,
    turquoise, violet, wheat, white, whitesmoke, yellow, yellowgreen,
    Font, FontStyle, FontWeight,
    Style, fill, stroke, join,
    LEFT, CENTER, RIGHT, TOP, MIDDLE, BOTTOM,
    Image, Point,
    empty, rectangle, square, ellipse, circle, line,
    triangle, right_triangle, isosceles_triangle,
    rhombus, regular_polygon, polygon, star_polygon, star, radial_star,
    text,
    width, height, dimension, center,
    rotate, scale, scale_xy, flip_horizontal, flip_vertical, frame, color_frame,
    crop, crop_align,
    above, beside,
    overlay, overlay_xy,
    underlay, underlay_xy,
    empty_scene, empty_scene_color,
    place_image, place_images, put_image,
    add_line, add_polygon, add_curve, add_solid_curve,
    to_pdf,
)
]]

local function split(text)
    local s, e = text:find("\n\n", 1, true)
    if s then
        return text:sub(1, s - 1), text:sub(e + 1)
    else
        return "", text
    end
end

local function strip_prompt(line)
    -- remove um prefixo ">>> " (ou ">>>") ou "... " (ou "...") da linha
    if line:sub(1, 4) == ">>> " then
        return line:sub(5)
    elseif line:sub(1, 3) == ">>>" then
        return line:sub(4)
    elseif line:sub(1, 4) == "... " then
        return line:sub(5)
    elseif line:sub(1, 3) == "..." then
        return line:sub(4)
    end
    return line
end

local function strip_prompts(text)
    local lines = {}
    for line in (text .. "\n"):gmatch("([^\n]*)\n") do
        table.insert(lines, strip_prompt(line))
    end
    -- remove a linha vazia final adicionada por causa do `text .. "\n"`
    if lines[#lines] == "" then
        table.remove(lines)
    end
    return table.concat(lines, "\n")
end

local function file_read(path)
    local f = io.open(path, "rb")
    if not f then return nil end
    local content = f:read("*all")
    f:close()
    return content
end

local function file_size(path)
    local f = io.open(path, "rb")
    if not f then return 0 end
    local size = f:seek("end") or 0
    f:close()
    return size
end

local function file_mtime(path)
    local f = io.popen("stat -c %Y '" .. path .. "' 2>/dev/null")
    if not f then return 0 end
    local v = f:read("*a")
    f:close()
    return tonumber(v) or 0
end

function CodeBlock(el)
    if not el.classes:includes("python-image") then
        return el
    end
    cont = cont + 1
    local name = "i" .. tostring(cont)
    local hide, content = split(el.text)

    -- expressão a renderizar: remove os prompts ">>> " e "... " de todas as linhas
    local expr = strip_prompts(content)

    local py = "target/spython_images/" .. name .. ".py"
    local pdf = "target/spython_images/" .. name .. ".pdf"
    -- sufixos de arquivos temporários únicos por processo (evita race entre
    -- builds paralelos: slides + handout + tex compartilham os mesmos iN.*)
    local tag = UUID .. "." .. tostring(cont)
    local py_tmp = py .. "." .. tag .. ".tmp"
    local pdf_tmp = pdf .. "." .. tag .. ".tmp"
    os.execute("mkdir -p ../target/spython_images/")

    -- monta o conteúdo do .py em memória para podermos comparar com o existente
    local py_content = "import sys\n" .. IMPORTS .. "\n"
    if hide ~= "" then
        py_content = py_content .. hide .. "\n"
    end
    py_content = py_content .. "sys.stdout.buffer.write(to_pdf((\n" .. expr .. "\n)))\n"

    -- pula se .py já existe com mesmo conteúdo e .pdf já está pronto e não vazio
    local up_to_date = file_read("../" .. py) == py_content
        and file_size("../" .. pdf) > 0

    if not up_to_date then
        local fpy = io.open("../" .. py_tmp, "w")
        fpy:write(py_content)
        fpy:close()
        os.execute("mv ../" .. py_tmp .. " ../" .. py)
        -- Run spython into a private tmp PDF, then atomically rename. The mv
        -- guards against races between parallel builds (slides + handout + tex
        -- share the same iN.pdf).
        os.execute("cd ../ && spython run -l 5 " .. py .. " > " .. pdf_tmp .. " 2>/dev/null"
            .. " && mv " .. pdf_tmp .. " " .. pdf)
    end

    return {
        pandoc.CodeBlock(content, {class = "python-repl"}),
        pandoc.Para{pandoc.Image({}, "../" .. pdf)}
    }
end

-- Imagens cuja fonte termina em ".py" são geradas pelo spython em tempo de
-- build: o script é executado e seus bytes em stdout são gravados como PDF,
-- que substitui o caminho da imagem. O .py deve ser auto-contido (incluir
-- imports e chamar `sys.stdout.buffer.write(to_pdf(...))` no final).
function Image(el)
    local src = el.src
    if not src or not src:match("%.py$") then
        return el
    end

    -- src é relativo ao diretório do capítulo (cwd do pandoc).
    -- Slug derivado do caminho para não colidir com blocos inline (iN.pdf).
    local slug = "file_" .. src:gsub("/", "_"):gsub("%.py$", "")
    local pdf = "target/spython_images/" .. slug .. ".pdf"
    local tag = UUID .. "." .. slug
    local pdf_tmp = pdf .. "." .. tag .. ".tmp"

    os.execute("mkdir -p ../target/spython_images/")

    -- Regenera quando o .py é mais novo que o .pdf cacheado (ou .pdf não existe).
    if file_mtime(src) > file_mtime("../" .. pdf) then
        os.execute("spython run -l 5 " .. src .. " > ../" .. pdf_tmp .. " 2>/dev/null"
            .. " && mv ../" .. pdf_tmp .. " ../" .. pdf)
    end

    el.src = "../" .. pdf
    return el
end
