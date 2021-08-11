FROM python:3

RUN adduser --disabled-password --gecos '' metretrim_user

WORKDIR /usr/src/app

COPY MetReTrim .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

USER metretrim_user

ENTRYPOINT ["python","./MetReTrim"]

