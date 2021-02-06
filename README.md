# Django Samples

# sw version
```bash
$ sw_vers
ProductName:	macOS
ProductVersion:	11.1
BuildVersion:	20C69

$ python -V
Python 3.8.0
```
# create gitignore template
```bash
$ curl https://www.toptal.com/developers/gitignore/api/django >> .gitignore
```

# setup
```bash
$ python -m venv env
$ source env/bin/activate
export PATH=$PWD/env/bin:$PATH
$ pip install django==3.1.3
```

# creare project & app
```bash
$ django-admin startproject confug .
$ django-admin startapp samplecrud
$ mkdir templates
```

# and more...
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

# docker
```bash
$ docker build -t sample-generic-view/haku-mai:1.0 .

$ docker images sample-generic-view/haku-mai
REPOSITORY                     TAG       IMAGE ID       CREATED              SIZE
sample-generic-view/haku-mai   1.0       25b082550343   About a minute ago   77.4MB

$ docker run --rm -p 8000:8000 --name haku-mai-sample sample-generic-view/haku-mai:1.0
```