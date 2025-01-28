FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r Requirements.txt

EXPOSE 5000

# ENV NAME StageSync

CMD ["python", "-m", "flask", "--app", "server", "run"]
