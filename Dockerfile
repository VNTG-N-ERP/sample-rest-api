FROM python:3.9.5

WORKDIR /home/

RUN echo "git clone update - 111"

RUN git clone https://github.com/VNTG-N-ERP/sample-rest-api.git

WORKDIR /home/sample-rest-api

RUN pip install -r requirements.txt

RUN pip install gunicorn

EXPOSE 8000

CMD ["bash", "-c", "gunicorn common.wsgi --env DJANGO_SETTINGS_MODULE=common.settings.deploy --bind 0.0.0.0:8000"]
