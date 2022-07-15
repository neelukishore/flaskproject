FROM python:3.8
WORKDIR /home/app
COPY . /home/app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]