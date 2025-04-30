from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from code_automation.tools.custom_tool import read_from_markdown, save_to_markdown

@CrewBase
class CodeAutomation():
    """CodeAutomation crew"""

    @agent
    def thinker(self) -> Agent:
        return Agent(
            config=self.agents_config['software_thinker'],
            llm=LLM(
                model="ollama/llama3:70b",
                base_url="http://localhost:11434"
            ),
            model_kwargs={"temperature": 0.5},
            tools=[save_to_markdown],
            verbose=True
        )

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['solution_architect'],
            llm=LLM(
                model="ollama/deepseek-coder-v2:6.7b",
                base_url="http://localhost:11434"
            ),
            model_kwargs={"temperature": 0.3},
            tools=[read_from_markdown, save_to_markdown],
            verbose=True
        )

    @task
    def think_task(self) -> Task:
        return Task(
            config=self.tasks_config['think_task']
        )

    @task
    def architect_task(self) -> Task:
        return Task(
            config=self.tasks_config['architect_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CodeAutomation crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
