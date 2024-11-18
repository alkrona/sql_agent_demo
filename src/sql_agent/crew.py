from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import check_sql,list_tables,tables_schema,execute_sql
# Uncomment the following line to use an example of a custom tool
# from sql_agent.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SqlAgent():
	"""SqlAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def sql_dev(self) -> Agent:
		return Agent(
			config=self.agents_config['sql_dev'],
			allow_delegation=False,
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			tools=[list_tables,tables_schema,execute_sql,check_sql]
		)

	@agent
	def data_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['data_analyst'],
			allow_delegation=False,
			verbose=True
		)
	@agent
	def report_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['report_writer'],
			allow_delegation=False,
			verbose=True
		)

	@task
	def extract_data(self) -> Task:
		return Task(
			config=self.tasks_config['extract_data'],
		)

	@task
	def analyze_data(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_data'],
			#context=[self.extract_data]
		)

	@task
	def write_report(self) -> Task:
		return Task(
			config=self.tasks_config['write_report'],
			#context=[self.analyze_data],
			output_file="report.md"
		)
	@crew
	def crew(self) -> Crew:
		"""Creates the SqlAgent crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
