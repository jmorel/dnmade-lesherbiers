dev: clean build
	python scripts/dev.py

build:
	mkdir -p _build
	sass src/sass/index.scss _build/style.css
	cp src/css/normalize.css _build/normalize.css
	cp src/img/* _build/
	python scripts/templatize.py

clean:
	rm -rf _build