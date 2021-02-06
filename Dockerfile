# python3.8 on alpine pull image
FROM python:3.8-alpine

# Configuration working dir
WORKDIR /usr/src/app

# Configuration environments
# Prevent writing to pyc files and discs
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# Copy requirements to container's working directory
# and pip install
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the host's current directory to container's working directory
COPY . /usr/src/app/ 

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
