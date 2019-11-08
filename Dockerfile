FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p ./app
WORKDIR app

COPY . .

RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip wheel
RUN pip install --upgrade -r requirements.txt
RUN pip install --upgrade -r requirements.dev.txt

CMD bash -c "flask run --host='0.0.0.0'"