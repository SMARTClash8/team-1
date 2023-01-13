# start by pulling the python image
#docker pull tensorflow/tensorflow
FROM tensorflow/tensorflow
#python:3.9-alpine3.16

RUN mkdir /app
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 8000

# Run the image as a non-root user
#RUN adduser -D myuser
#USER myuser

CMD python manage.py runserver
