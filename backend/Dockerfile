FROM python:3.11-bullseye

RUN pip install "poetry==1.1.7"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 8001

# CMD ["poetry", "run", "python", "app.py"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=8001"]
