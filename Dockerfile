from python:3.8

WORKDIR /code

COPY . .
RUN pip install google-cloud-vision
RUN pip install google-cloud-speech
RUN pip install google-cloud-translate


CMD ["python", "./google_speech.py"]