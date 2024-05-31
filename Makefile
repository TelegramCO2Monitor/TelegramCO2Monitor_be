# Python virtual environment setup
create_venv:
	python3.12 -m venv venv && source venv/bin/activate

# Install dependencies
install:
	pip install --upgrade pip && pip install -r src/requirements.txt