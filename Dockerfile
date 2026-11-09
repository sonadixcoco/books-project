FROM python:3.11.10-slim 
WORKDIR /app 
COPY . /app 
CMD ["python", "app.py"] 
