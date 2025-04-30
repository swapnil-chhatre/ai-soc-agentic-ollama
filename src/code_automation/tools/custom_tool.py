from crewai.tools import tool
import datetime

@tool
def save_to_markdown(agent_name: str, path: str, filename: str, text: str) -> str:
    """
    Saves job titles and descriptions to a markdown file

    Args:
        agent_name: The name of the agent that generated the text.
        path: Location to save markdown file
        filename: Name of markdown file
        text: The text to save.

    Returns:
        A message indicating the file has been saved.
    """
    try:
        with open(path + filename, "w", encoding="utf-8") as f:
            f.write(text)
            f.write("\n\nEntry time: " + str(datetime.datetime.now()))
        return f"Text saved to {filename}"
    except Exception as e:
        return f"Error saving to {filename}: {e}"

@tool
def read_from_markdown(path: str, filename: str) -> str:
    """
    Reads content from a markdown file
    Args:
        path: Location of markdown file
        filename: Name of markdown file
    Returns:
        The content of the markdown file as a string.
    """
    try:
        with open(path + filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading content: {e}"