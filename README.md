# sample-rest-api

SHE 사전 개발용 RESTful API 서비스

## 기존 소스를 받을 경우

가상환경 생성 (프로젝트 루트에서 실행)  
python 가상환경 이름 -> `venv`

```bash
$ python3 -m venv devenv
$ source ./devenv/bin/activate
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

package 목록 저장 (가상환경/프로젝트 루트에서 실행)

```bash
(venv) $ pip freeze > requirements.txt
```

