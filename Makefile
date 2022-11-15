hello:
	python -m coverage run -m unittest discover -v -s ./src -p *test.py
	python -m coverage report && python -m coverage html