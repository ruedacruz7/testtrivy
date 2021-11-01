#FROM python:3
FROM python:3.7-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3","-u","./app.py" ]
