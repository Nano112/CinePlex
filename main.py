import imp
import pyautogui
from flask import Flask
from time import sleep
from VLC import VLC 
app = Flask(__name__)
player = VLC()


@app.route("/join")
def join():
    player.addPlaylist()
    pyautogui.getWindowsWithTitle("discord")[0].maximize()
    sleep(0.1)
    channel_location = get_channel_location()
    pyautogui.moveTo(channel_location)
    pyautogui.click()
    stream_button_location = get_stream_button_location()
    pyautogui.moveTo(stream_button_location)
    pyautogui.click()
    player.play()
    return "Hello World!"

def get_channel_location():
    return pyautogui.locateOnScreen("assets/channel.png")

def get_stream_button_location():
    return pyautogui.locateOnScreen("assets/stream_button.png")