#!/usr/bin/env python
import os
import sys
import warnings

# Add root path so code_automation package is importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from code_automation.crew import CodeAutomation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def load_user_topic():
    """
    Reads user_preference.txt and extracts the topic of interest.
    Defaults to 'AI tools for developers' if file or value is missing.
    """
    try:
        with open("knowledge/user_preference.txt", "r") as f:
            for line in f:
                if "interested in" in line.lower():
                    return line.split("in")[-1].strip().replace(".", "")
    except Exception as e:
        print(f"⚠️ Could not load user preferences: {e}")
    return "AI tools for developers"

def run():
    topic = load_user_topic()
    ideas_file_path = "outputs/"
    plan_files_folder = "outputs/plans/"

    os.makedirs(ideas_file_path, exist_ok=True)
    os.makedirs(plan_files_folder, exist_ok=True)

    inputs = {
        "topic": topic,
        "ideas_file_path": ideas_file_path,
        "plan_files_folder": plan_files_folder,
        "code_output_path": os.path.join(ideas_file_path, "final_code.md"),
        "idea_name": "Personalized Task Automator"
    }

    try:
        result = CodeAutomation().crew().kickoff(inputs=inputs)
        print("\n✅ Final Result:")
        print(result)
    except Exception as e:
        print(f"❌ Error while running the crew: {e}")
        raise


if __name__ == "__main__":
    run()
