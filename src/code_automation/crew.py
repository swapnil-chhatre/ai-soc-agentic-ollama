from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.llm import LLM
#from crewai import CrewContext  # NEW: for runtime inputs

from code_automation.tools.custom_tool import read_from_markdown, save_to_markdown

@CrewBase
class CodeAutomation():
    """CodeAutomation Crew - Idea Generator -> Architect -> Code Optimizer"""

    @agent
    def thinker(self) -> Agent:
        return Agent(
            config=self.agents_config['software_thinker'],
            llm=LLM(
                model="ollama/deepseek-coder-v2:latest",
                base_url="http://localhost:11434"
            ),
            model_kwargs={"temperature": 0.7},
            tools=[save_to_markdown],
            verbose=True
        )

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['solution_architect'],
            llm=LLM(
                model="ollama/deepseek-coder-v2:latest",
                base_url="http://localhost:11434"
            ),
            model_kwargs={"temperature": 0.4},
            tools=[save_to_markdown],
            verbose=True
        )

    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config['coding_expert'],
            llm=LLM(
                model="ollama/deepseek-coder-v2:latest",
                base_url="http://localhost:11434"
            ),
            model_kwargs={"temperature": 0.2},
            tools=[read_from_markdown, save_to_markdown],
            verbose=True
        )

    @task
    def think_task(self) -> Task:
        return Task(
            config=self.tasks_config['software_thinking_task'],
            agent=self.thinker()
        )

    @task
    def architect_task(self) -> Task:
        return Task(
            config=self.tasks_config['solution_architect_task'],
            agent=self.architect()
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_optimization_task'],
            agent=self.coder()
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
