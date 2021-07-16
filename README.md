hello-flask
===
Python Flask and honcho + gunicorn Test Program

## PyPI
```shell
$ pip install Flask gunicorn honcho
$ pip freeze > requirements.txt 
```

## Docker
- Based Docker Image: [python official image](https://hub.docker.com/_/python)
```shell
$ docker build -t marmotte/hello-flask .
$ docker run -it --rm -p 5000:5000 --name hello-flask marmotte/hello-flask
```
