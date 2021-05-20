FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
USER 1001
ENTRYPOINT ["python"]
CMD ["app.py"]
