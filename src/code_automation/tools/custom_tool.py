from crewai.tools import tool
import datetime
import os

@tool("save_to_markdown")
def save_to_markdown(agent_name: str, path: str, filename: str, text: str) -> str:
    """
    Saves text to a markdown file with a timestamp.

    Args:
        agent_name: The name of the agent that generated the text.
        path: Folder to save the markdown file in.
        filename: Markdown filename (e.g. idea1.md).
        text: The content to save.

    Returns:
        Success or error message.
    """
    try:
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, filename)

        content = f"{text}\n\n---\nSaved by {agent_name} at {datetime.datetime.now().isoformat()}\n"

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[✅ save_to_markdown] File saved: {full_path}")
        return f"✅ Markdown saved to `{full_path}`"
    except Exception as e:
        error_message = f"❌ Error saving to `{filename}`: {str(e)}"
        print(f"[❌ save_to_markdown] {error_message}")
        return error_message


@tool("read_from_markdown")
def read_from_markdown(path: str, filename: str) -> str:
    """
    Reads text from a markdown file.

    Args:
        path: Folder where the markdown file is.
        filename: Markdown filename.

    Returns:
        File content or error message.
    """
    try:
        full_path = os.path.join(path, filename)

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f"[📄 read_from_markdown] File read: {full_path}")
        return content
    except Exception as e:
        error_message = f"❌ Error reading from `{filename}`: {str(e)}"
        print(f"[❌ read_from_markdown] {error_message}")
        return error_message
