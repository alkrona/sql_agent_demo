# SqlAgent Crew

Welcome to the SqlAgent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/sql_agent/config/agents.yaml` to define your agents
- Modify `src/sql_agent/config/tasks.yaml` to define your tasks
- Modify `src/sql_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/sql_agent/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the sql_agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The sql_agent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Resources
-[Create and Populate DB with fake data with Faker ](https://python.plainenglish.io/generating-a-fake-database-with-python-8523bf6db9ec)

-[PostgresDB to SQL server migration](https://www.mssqltips.com/sqlservertip/2619/export-data-from-postgres-to-sql-server-using-ssis/)

-[Fast Api for crew AI setup](https://www.youtube.com/watch?v=pFZHpFuzcBE)

-[Azure Container Apps for Container deployment](https://www.youtube.com/watch?v=2q_EA98kDGg)

-[Docker configuration on VM](https://knowledgebase.aridhia.io/workspaces/analysing-data/virtual-machines/installing-software-on-virtual-machines/installing-docker-on-your-virtual-machine)