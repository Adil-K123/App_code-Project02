FROM python:3.10.14-alpine3.20
EXPOSE 8000
WORKDIR /flask_app

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:app"]

