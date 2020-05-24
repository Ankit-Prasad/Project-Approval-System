FROM python:3.8-slim-buster

# File Author
MAINTAINER Ankit Prasad

# Copies the files from the source on the host into the container’s set destination
COPY . /app
RUN mkdir /app/uploads



#ENTRYPOINT runs the as the first command when container is created
RUN apt-get -y update
RUN apt-get install -y sqlite3
RUN pip3 install flask



EXPOSE 5001

CMD ["sh", "-c", "python3 app/table.py && python3 app/module.py"]
