FROM python:3.7-alpine
WORKDIR /usr/src/app/backend
COPY requirements*.txt ./
RUN pip install -r requirements.txt
COPY . .