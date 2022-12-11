## test: runs all tests
test: 
	@python3 -m pytest -v

## build: build and creates an executable program for application.
build: clean
	@pyinstaller -F ./main/app.py -n app --specpath ./spec -p .

## clean: cleans previous build
clean:
	@echo "Cleaning..."
	@- rm -f -r ./dist ./spec ./build
	@echo "Cleaned!"
