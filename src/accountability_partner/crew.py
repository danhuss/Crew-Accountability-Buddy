from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AccountabilityPartner():
	"""AccountabilityPartner crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def coach_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['coach_agent'],
			verbose=True,
			allow_delegation=True
		)
	
	@agent
	def tracker_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['tracker_agent'],
			verbose=True,
			allow_delegation=False
		)
	
	@agent
	def expert_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['expert_agent'],
			verbose=True,
			allow_delegation=False
		)
	
	@agent
	def reflection_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['reflection_agent'],
			verbose=True,
			allow_delegation=False
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def initial_assessment_task(self) -> Task:
		return Task(
			config=self.tasks_config['initial_assessment_task'],
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the AccountabilityPartner crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
			# planning=True,
			# manager_agent=an_agent,
			# manager_llm=some_llm,
			# knowledge_sources=[],
		)
