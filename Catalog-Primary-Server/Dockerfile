FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ARG DEFAULT_PORT=9000

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

CMD python3 manage.py runserver 0.0.0.0:$PORT