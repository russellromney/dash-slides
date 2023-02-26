FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--worker-class","gevent","--workers","2","--worker-connections=500","app:server", "-b", "0.0.0.0:8080"]