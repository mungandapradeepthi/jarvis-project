import webbrowser
import pyautogui
import time
import wikipedia
from assistant.ai_brain import ask_ai


def execute_command(command):

    command = command.lower()

    # -----------------------------
    # OPEN CHROME + SEARCH
    # -----------------------------

    if "open chrome and search" in command:

        search_query = command.replace(
            "open chrome and search",
            ""
        ).strip()

        url = f"https://www.google.com/search?q={search_query}"

        webbrowser.open(url)

        return f"Searching {search_query} on Google"

    # -----------------------------
    # SEARCH DIRECTLY
    # -----------------------------

    elif command.startswith("search "):

        search_query = command.replace(
            "search",
            ""
        ).strip()

        url = f"https://www.google.com/search?q={search_query}"

        webbrowser.open(url)

        return f"Searching {search_query}"

    # -----------------------------
    # OPEN YOUTUBE + SEARCH
    # -----------------------------

    elif "open youtube and search" in command:

        search_query = command.replace(
            "open youtube and search",
            ""
        ).strip()

        url = f"https://www.youtube.com/results?search_query={search_query}"

        webbrowser.open(url)

        return f"Searching YouTube for {search_query}"

    # -----------------------------
    # OPEN GOOGLE
    # -----------------------------

    elif "open google" in command:

        webbrowser.open("https://google.com")

        return "Opening Google"

    # -----------------------------
    # OPEN YOUTUBE
    # -----------------------------

    elif "open youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    # -----------------------------
    # OPEN CHATGPT
    # -----------------------------

    elif "open chatgpt" in command:

        webbrowser.open("https://chat.openai.com")

        return "Opening ChatGPT"

    # -----------------------------
    # OPEN CHROME
    # -----------------------------

    elif "open chrome" in command:

        webbrowser.open("https://google.com")

        return "Opening Chrome"

    # -----------------------------
    # WIKIPEDIA
    # -----------------------------

    elif "who is" in command or "what is" in command:

        try:

            topic = command.replace("who is", "")
            topic = topic.replace("what is", "")

            info = wikipedia.summary(
                topic,
                sentences=2
            )

            return info

        except:

            return ask_ai(command)

    # -----------------------------
    # CLOSE WINDOW
    # -----------------------------

    elif "close window" in command:

        pyautogui.hotkey("alt", "f4")

        return "Closing window"

    # -----------------------------
    # MINIMIZE WINDOW
    # -----------------------------

    elif "minimize window" in command:

        pyautogui.hotkey("win", "down")

        return "Minimizing window"

    # -----------------------------
    # TYPE MODE
    # -----------------------------

    elif "type" in command:

        text = command.replace("type", "")

        pyautogui.write(text)

        return f"Typing {text}"

    # -----------------------------
    # AI CHAT
    # -----------------------------

    else:

        return ask_ai(command)