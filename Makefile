MAIN=./main.py
SRCS=$(filter-out $(MAIN), $(wildcard ./*.py))

ICON=./res/icon.ico

run: $(MAIN) $(SRCS)
	python $<

build: $(MAIN) $(SRCS)
	pyinstaller --onefile --noconsole --icon=$(ICON) $^

clean:
	rm -rf __pycache__