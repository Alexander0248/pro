FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /prod

RUN pip install --upgrade pip "poetry==2.4.1"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY mysite .

CMD ["sh", "-c", "python manage.py migrate && gunicorn mysite.wsgi:application --bind 0.0.0.0:8000"]
