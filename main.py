from threading import Thread
import json
import os

from assistant.voice import listen
from assistant.speak import speak
from assistant.commands import execute_command

from gui.interface import JarvisGUI


gui = JarvisGUI()

conversation_mode = "TEXT"


# =========================
# SAVE CHAT MEMORY
# =========================

MEMORY_FILE = "data/memory.json"


def save_conversation(user, jarvis):

    memory = []

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as file:

            try:
                memory = json.load(file)

            except:
                memory = []

    memory.append({

        "user": user,
        "jarvis": jarvis

    })

    with open(MEMORY_FILE, "w") as file:

        json.dump(memory, file, indent=4)


# =========================
# PROCESS COMMAND
# =========================

def process_command(command):

    global conversation_mode

    command = command.lower()

    # MODE SWITCHING

    if "voice mode" in command:

        conversation_mode = "VOICE"

        response = "Voice mode activated"

        gui.update_chat(f"Jarvis: {response}")

        speak(response)

        return

    elif "text mode" in command:

        conversation_mode = "TEXT"

        response = "Text mode activated"

        gui.update_chat(f"Jarvis: {response}")

        speak(response)

        return

    # NORMAL CHAT

    gui.update_chat(f"You: {command}")

    gui.update_status("PROCESSING")

    response = execute_command(command)

    gui.update_chat(f"Jarvis: {response}")

    save_conversation(command, response)

    gui.update_status("ONLINE")


# =========================
# VOICE LOOP
# =========================

def voice_loop():

    speak("Jarvis system activated")

    while True:

        try:

            if conversation_mode == "VOICE":

                gui.update_status("LISTENING")

                command = listen()

                if command and len(command) > 1:

                    process_command(command)

        except Exception as e:

            print("Voice Loop Error:", e)


# =========================
# START SYSTEM
# =========================

gui.set_input_callback(process_command)

Thread(target=voice_loop, daemon=True).start()

gui.run()