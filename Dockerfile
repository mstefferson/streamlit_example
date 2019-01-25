FROM manifoldai/orbyter-ml-dev:1.1
ADD requirements.txt /mnt/requirements.txt
WORKDIR /mnt/
RUN apt-get update &&\
pip install --upgrade pip &&\
pip install -r requirements.txt
