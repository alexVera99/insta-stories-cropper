FROM python:3.8.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update ##
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
