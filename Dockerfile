FROM python:3.9.18-alpine
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir python
# WORKDIR /python
# CMD ["/bin/sh"]