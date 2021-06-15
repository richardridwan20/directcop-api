FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

# EXPOSE $APP_PORT
WORKDIR /app

RUN apt-get update \
        && apt-get install gcc -y \
        && apt-get install libc-dev -y \
        && apt-get install default-mysql-server -y \
        && apt-get install default-libmysqlclient-dev -y \
        && apt-get install python3-dev  -y \
        && apt-get install openssl -y \
        && apt-get install libssl-dev -y \
        && apt-get install build-essential -y \
        && apt-get clean

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . ./

CMD ["mysql"]
CMD pip install alembic
CMD ["alembic","upgrade","head"]

# command to run on container start
CMD pip install -r requirements.txt && \
    pip install mysql-connector && \
    pip install alembic && \
    pip install pydantic[dotenv] && \
    pip install mysqlclient && \
    pip install passlib && \
    PYTHONPATH=. alembic upgrade head && \
    python main.py