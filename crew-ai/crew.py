from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class SocialMediaCrew():
    """
    A crew that excels in creating social media content.
    """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"]
        )

    @agent
    def expert(self) -> Agent:
        return Agent(
            config=self.agents_config["expert"]
        )
    
    @agent
    def media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["media_manager"]
        )
    
    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config["research"]
        )
    
    @task
    def extract_tags(self) -> Task:
        return Task(
            config=self.tasks_config["extract_tags"],
            context=[self.research()]
        )
    
    @task
    def writing(self) -> Task:
        return Task(
            config=self.tasks_config["writing"],
            context=[self.extract_tags()]
        )
    
    @task
    def summarize_to_post(self) -> Task:
        return Task(
            config=self.tasks_config["summarize_to_post"],
            context=[self.writing(), self.extract_tags()]
        )
    
    @task
    def suggest_material(self) -> Task:
        return Task(
            config=self.tasks_config["suggest_material"],
            context=[self.research(), self.writing()]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )
