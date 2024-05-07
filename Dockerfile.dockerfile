FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
WORKDIR /usr/app/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD python flask_app.py