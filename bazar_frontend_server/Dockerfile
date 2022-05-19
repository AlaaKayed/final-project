FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 4200

EXPOSE $PORT

CMD python3 manage.py runserver 0.0.0.0:$PORT