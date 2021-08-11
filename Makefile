test:
	pytest tests/

lint:
	flake8 tests/

format:
	black tests/ 

