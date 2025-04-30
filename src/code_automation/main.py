#!/usr/bin/env python
import sys
import warnings
import os
import yaml

from code_automation.crew import CodeAutomation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():

    """
    Run the crew.
    """
    inputs={
        "topic": input_config['job_title'],
        "ideas_file_path": '/home/user/ai-soc-ollama-agents/code_automation/src/code_automation/',
        "plan_files_folder": '/home/user/ai-soc-ollama-agents/code_automation/src/plans/'
    }
    
    try:
        CodeAutomation().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")