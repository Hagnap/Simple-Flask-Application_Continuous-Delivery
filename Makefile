install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py
    
run: 
	python main.py

all: 
	install lint test