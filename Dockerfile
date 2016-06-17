FROM python:3.5-alpine
RUN apk add --no-cache git make perl
ADD ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 5000
CMD ["./start.sh"]