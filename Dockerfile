FROM python:3.9

COPY src /app/src
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD [ "python", "-m" , "flask", "--app=app/src/app", "run", "--host=0.0.0.0"]
