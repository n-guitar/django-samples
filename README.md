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