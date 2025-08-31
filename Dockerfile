FROM python:3.12-slim AS builder

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.8.2
RUN python -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION

ENV PATH="$POETRY_HOME/bin:$PATH"

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.in-project true

RUN poetry install --no-interaction --no-ansi --no-root --no-dev

FROM python:3.12-slim AS final

WORKDIR /app

RUN addgroup --system app && adduser --system --group app
USER app

COPY --from=builder /app/.venv ./.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY ./src/cle ./src/cle

EXPOSE 8000

CMD ["uvicorn", "src.cle.main:app", "--host", "0.0.0.0", "--port", "8000"]
