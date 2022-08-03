# pull official base image
FROM python:3.9


# set work directory
WORKDIR /usr/src/mailing_service
ADD . /usr/src/mailing_service

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/mailing_service/docker-entrypoint.sh

COPY . /usr/src/mailing_service

ENTRYPOINT ["/usr/src/mailing_service/docker-entrypoint.sh"]