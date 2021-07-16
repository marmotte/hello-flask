FROM python:3.7.10-alpine
MAINTAINER Yosuke Yamamoto

ENV LANG en_US.UTF-8
ENV TZ Asia/Tokyo

## Update Environments
RUN apk update \
    && apk add --no-cache gcc git python3-dev musl-dev \
    linux-headers libc-dev libxml2-dev libxslt-dev \
    &&  pip install --upgrade pip

## Deplyments
WORKDIR /usr/src/app
ADD / /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["honcho", "start"]
