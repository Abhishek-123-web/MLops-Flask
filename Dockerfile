FROM python:3.8-slim-buster

WORKDIR /flask-loan-app 
# this is the directory inside the container

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .


# python3 flask --app app.py run
CMD ["python3", "-m", "flask", "--app", "app.py", "run", "--host=0.0.0.0"]

