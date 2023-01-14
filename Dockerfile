# start by pulling the python image
#docker pull tensorflow/tensorflow
FROM continuumio/miniconda3
# FROM continuumio/conda-ci-linux-64-python3.8:latest
#python:3.9-alpine3.16
#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
USER root
ARG conda_env=myenv
RUN mkdir /tmp/app
# switch working directory
WORKDIR /usr/home/app

ADD ./environment.yml ./environment.yml
RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env

# copy the requirements file into the image
COPY ./requirements.txt /usr/home/app/requirements.txt

# install the dependencies and packages in the requirements file
RUN conda config --env --add channels conda-forge
RUN conda install --file requirements.txt
# copy every content from the local file to the image
COPY . /usr/home/app

EXPOSE 8000

# The code to run when container is started:
ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "manage.py", "runserver"]
# Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Run the image as a non-root user
#RUN adduser -D myuser
#USER myuser
#ENTRYPOINT [ "/bin/sh", "-l", "-c" ]
#RUN python --version
#CMD python manage.py runserver 0.0.0.0:8000
# CMD python /usr/home/app/manage.py runserver 0.0.0.0:8000
