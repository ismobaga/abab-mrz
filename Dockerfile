FROM python:3

# MAINTANER  Ismail "ismail@bagayoko.ml"

    
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install tesseract-ocr -y
# RUN git clone https://github.com/ismobaga/tesseractMRZ.git
COPY ./mrz.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

EXPOSE 5000 5000
CMD ["flask", "run"]