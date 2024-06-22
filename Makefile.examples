.PHONY: check

SOURCES := $(shell fdfind -e py )

check:
	mypy --check-untyped-defs ${SOURCES}
	python -B -m doctest ${SOURCES}
