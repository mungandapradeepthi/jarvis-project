import speech_recognition as sr


recognizer = sr.Recognizer()

recognizer.energy_threshold = 400

recognizer.pause_threshold = 1.2


def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

            print("Recognizing...")

            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You said:", command)

            return command.lower()

    except sr.WaitTimeoutError:

        return ""

    except sr.UnknownValueError:

        return ""

    except Exception as e:

        print("Voice Error:", e)

        return ""