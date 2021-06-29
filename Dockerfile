FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

WORKDIR /home/

# GitHub 캐시를 해결하기 위한 임시 문자열 출력 - github 소스 변경 시 아래 숫자 변경 요망 -> 해결 방안 필요
RUN echo "git clone update - 111"

# django app 받기 (GitHub -> Docker images) -> 추후 ssh 인증 적용 필요
RUN git clone https://github.com/VNTG-N-ERP/sample-rest-api.git

WORKDIR /home/sample-rest-api

# django app 설정 파일 복사
COPY settings.ini /home/sample-rest-api/settings.ini

# django 종속 패키지 설치
RUN pip install -r requirements.txt

# django wsgi 패키지 설치
RUN pip install gunicorn

# RUN python manage.py collectstatic

EXPOSE 8000

# CMD ["gunicorn", "common.wsgi", "--bind", "0.0.0.0:8000"]

# CMD ["bash", "-c", "gunicorn common.wsgi --bind 0.0.0.0:8000"]
# static 파일을 staticfiles 폴더에 모으고, gunicorn을 이용하여 app 실행
# CMD ["bash", "-c", "python manage.py collectstatic --noinput && gunicorn common.wsgi --bind 0.0.0.0:8000"]
# CMD ["bash", "-c", "gunicorn common.wsgi --bind 0.0.0.0:8000"]

# CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=common.settings.deploy && gunicorn common.wsgi --env DJANGO_SETTINGS_MODULE=common.settings.deploy --bind 0.0.0.0:8000"]
CMD ["bash", "-c", "gunicorn common.wsgi --env DJANGO_SETTINGS_MODULE=common.settings.deploy --bind 0.0.0.0:8000"]


