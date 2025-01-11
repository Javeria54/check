FROM python:3.9.18-slim

ADD . .

RUN pip3 install -r requirements.txt

EXPOSE 8008

CMD ["flask", "run", "--host=0.0.0.0", "--port=8008"]
