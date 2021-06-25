# sample-rest-api

SHE 사전 개발용 RESTful API 서비스

## 기존 소스를 받을 경우

가상환경 생성 (프로젝트 루트에서 실행)  
python 가상환경 이름 -> `venv`

```bash
$ python3 -m venv venv
$ source ./venv/bin/activate
```

package 복원 (가상환경에서 실행)

```bash
(venv) $ pip install -r requirements.txt
```

데이터베이스 초기화 (django project 폴더에서)

```bash
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
```

## 새로운 모듈을 설치한 경우

package 목록 저장 (가상환경에서 실행)

```bash
(venv) $ pip freeze > requirements.txt
```

## settings.ini 생성

레파지토리 루트 폴더에 `settings.ini` 파일을 생성하고 다음 내용을 채워서 저장합니다.

```
[settings]
SECRET_KEY=django-secret_key
POSTGRES_NAME=postgresql_db_name
POSTGRES_USER=postgresql_user_name
POSTGRES_PASSWORD=postgresql_user_password
POSTGRES_HOST=postgresql_ip_address
POSTGRES_PORT=5432
```

## Swagger UI

가상환경(venv)에서 어플리케이션 실행

```bash
(venv) $ python3 manage.py runserver
```

다음 url에 접속하여 swagger ui를 확인한다.

> http://127.0.0.1:8000/swagger

### drf-yasg를 이용한 swagger 문서 자동화

* 참고 - https://velog.io/@lu_at_log/drf-yasg-and-swagger

## Docker 이미지 생성 및 배포

### ssh