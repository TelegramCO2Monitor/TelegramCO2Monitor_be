# Python virtual environment setup
create_venv:
	python3.12 -m venv venv && source venv/bin/activate

# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Linting
lint:
	flake8 src

# Setup hooks
setup_hooks:
	python3.12 setup_hooks.py