FROM python:3
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8080
USER 1001
ENTRYPOINT ["python"]
CMD ["wsgi.py"]
