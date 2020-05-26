FROM python:3.6-alpine

# File Author
MAINTAINER Ankit Prasad

# Copies the files from the source on the host into the container’s set destination
COPY . /app
RUN mkdir /app/uploads



#ENTRYPOINT runs the as the first command when container is created
RUN pip3 install -r requirements.txt



EXPOSE 5001


CMD ["sh", "-c", "cd app && python3 module.py"]
