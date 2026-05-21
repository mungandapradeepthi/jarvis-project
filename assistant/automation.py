import webbrowser
import os


def open_youtube():
    webbrowser.open("https://youtube.com")


def open_google():
    webbrowser.open("https://google.com")


def open_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    os.startfile(chrome_path)