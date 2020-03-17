FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python certificate_generator.py