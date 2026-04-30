-- Filtro pandoc que renderiza blocos de código com classe `python-image`
-- como uma imagem gerada pelo spython.
--
-- O conteúdo do bloco pode ter duas partes separadas por uma linha em branco:
-- a primeira é "hide" (incluída no script mas não exibida no slide),
-- a segunda é o conteúdo exibido, cuja primeira linha começa com `>>> `
-- (e linhas de continuação com `... `) e contém a expressão final que é
-- passada para `to_svg`.
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
    to_svg,
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

-- Mirrors HtDP/2htdp/image's interactive bitmap renderer, which draws an
-- image of nominal size W x H onto a (W+1) x (H+1) bitmap so that 1px
-- outline strokes painted on the bbox boundary are not clipped. The
-- library's `to_svg` keeps the nominal W x H (matching `save-svg-image`
-- in Racket) because composition relies on those nominal sizes; we only
-- enlarge the outermost canvas at render time.
--
-- Whether the viewBox needs a -0.5 shift depends on the path coordinate
-- alignment used by the library:
--
--   * Default 1px outline-only paths use half-pixel coords (e.g. paths
--     starting at "M 0.5 0.5 ..."): the stroke fits in canvas pixel
--     boundaries with viewBox "0 0 W+1 H+1", crisp on all four edges.
--     Shifting the viewBox would land strokes mid-pixel and blur them.
--
--   * Everything else (filled+stroked, thick outline) uses integer
--     coords and the stroke straddles each bbox edge by half its width:
--     viewBox "-0.5 -0.5 W+1 H+1" gives breathing room equally on all
--     sides so the four edges render symmetrically.
--
-- We detect "default 1px outline-only" by looking for any path with
-- fill="none" and no stroke-width attribute. If found, we skip the
-- shift; otherwise we apply it.
local function has_default_outline(content)
    for tag in content:gmatch('<path[^/]-/>') do
        if tag:find('fill="none"', 1, true)
            and tag:find('stroke=', 1, true)
            and not tag:find('stroke-width=', 1, true) then
            return true
        end
    end
    return false
end

local function inflate_svg_canvas(path)
    local f = io.open(path, "rb")
    if not f then return end
    local content = f:read("*all")
    f:close()
    local w_str = content:match('<svg%s+width="([^"]+)"')
    local h_str = content:match('height="([^"]+)"')
    if not w_str or not h_str then return end
    local w = tonumber(w_str)
    local h = tonumber(h_str)
    if not w or not h then return end
    local nw = w + 1
    local nh = h + 1
    local vb_x, vb_y = 0.0, 0.0
    if not has_default_outline(content) then
        vb_x, vb_y = -0.5, -0.5
    end
    local new_header = string.format(
        '<svg width="%g" height="%g" viewBox="%g %g %g %g"',
        nw, nh, vb_x, vb_y, nw, nh)
    -- Replace the leading <svg ... xmlns="..."> opening tag.
    content = content:gsub('<svg[^>]*xmlns', new_header .. ' xmlns', 1)
    f = io.open(path, "wb")
    f:write(content)
    f:close()
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
    local svg = "target/spython_images/" .. name .. ".svg"
    local pdf = "target/spython_images/" .. name .. ".pdf"
    -- sufixos de arquivos temporários únicos por processo (evita race entre
    -- builds paralelos: slides + handout + tex compartilham os mesmos iN.*)
    local tag = UUID .. "." .. tostring(cont)
    local py_tmp = py .. "." .. tag .. ".tmp"
    local svg_tmp = svg .. "." .. tag .. ".tmp"
    local pdf_tmp = pdf .. "." .. tag .. ".tmp"
    os.execute("mkdir -p ../target/spython_images/")

    -- monta o conteúdo do .py em memória para podermos comparar com o existente
    local py_content = IMPORTS .. "\n"
    if hide ~= "" then
        py_content = py_content .. hide .. "\n"
    end
    py_content = py_content .. "print(to_svg((\n" .. expr .. "\n)))\n"

    -- pula se .py já existe com mesmo conteúdo e .pdf já está pronto e não vazio
    local up_to_date = file_read("../" .. py) == py_content
        and file_size("../" .. svg) > 0
        and file_size("../" .. pdf) > 0

    if not up_to_date then
        local fpy = io.open("../" .. py_tmp, "w")
        fpy:write(py_content)
        fpy:close()
        os.execute("mv ../" .. py_tmp .. " ../" .. py)
        -- Run spython into a private tmp; inflate the canvas so outline strokes
        -- at the bbox edges are not clipped (HtDP-style); then convert to PDF.
        -- The final atomic mv guards against races between parallel builds.
        os.execute("cd ../ && spython run -l 5 " .. py .. " > " .. svg_tmp .. " 2>/dev/null")
        inflate_svg_canvas("../" .. svg_tmp)
        os.execute("cd ../ && rsvg-convert --format pdf1.5 --output " .. pdf_tmp .. " " .. svg_tmp
            .. " && mv " .. svg_tmp .. " " .. svg
            .. " && mv " .. pdf_tmp .. " " .. pdf)
    end

    return {
        pandoc.CodeBlock(content, {class = "python-repl"}),
        pandoc.Para{pandoc.Image({}, "../" .. pdf)}
    }
end
