FROM python:3.12.2

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

RUN pip install uv
WORKDIR /app
COPY uv.lock pyproject.toml /app/

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project --no-dev
RUN pip install fastapi uvicorn python-dotenv crewai psycopg2
COPY . /app

ENV PYTHONPATH="/app/src/sql_agent:${PYTHONPATH}"
EXPOSE 80
CMD ["uvicorn","src.sql_agent.main:app","--host","0.0.0.0","--port","80"]