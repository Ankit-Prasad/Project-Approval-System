FROM python:3.6-alpine

# File Author
MAINTAINER Ankit Prasad

COPY . /app
RUN mkdir /app/uploads

RUN pip3 install -r /app/requirements.txt

EXPOSE 5001

CMD ["sh", "-c", "cd app && python3 module.py"]
