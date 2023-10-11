FROM python:3.9
WORKDIR /app
ENV FLASK_APP=app.py
COPY requirements.txt ./requirements
RUN pip install -r ./requirements
EXPOSE 5000
CMD [ "flask", "run" ]