FROM python:3.12.2

RUN apt-get update

RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc |  gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list |  tee /etc/apt/sources.list.d/mssql-release.list
  


RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
RUN . ~/.bashrc
RUN pip install uv

WORKDIR /app
COPY uv.lock pyproject.toml /app/

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project --no-dev
RUN pip install fastapi uvicorn python-dotenv crewai pyodbc 
COPY . /app

ENV PYTHONPATH="/app/src/sql_agent"

EXPOSE 80
CMD ["uvicorn","src.sql_agent.main:app","--host","0.0.0.0","--port","80"]