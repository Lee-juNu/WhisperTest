FROM python:3.9.7

WORKDIR /code

RUN apt update
RUN apt install ffmpeg -y
RUN pip install --upgrade pip

RUN pip install openai-whisper==20230314
RUN pip install setuptools-rust==1.5.2
RUN pip install numpy==1.26.4

COPY ./app /code/app