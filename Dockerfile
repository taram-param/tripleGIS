FROM python:3.12

WORKDIR /srv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install --no-install-recommends postgresql gcc libpq-dev\
  && apt-get -y install --no-install-recommends binutils libproj-dev gdal-bin \
  && apt-get clean

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .


CMD ["python", "manage.py", "migrate"]