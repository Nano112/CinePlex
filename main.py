import pyautogui
from flask import Flask
from time import sleep
import vlc
import os
app = Flask(__name__)
# creating vlc media player object
player = vlc.MediaPlayer()
 
path = r"./videos"
videos = os.listdir(path)
media = vlc.Media(os.path.join(path,videos[0]))
player.set_media(media)

@app.route("/join")
def join():
    sleep(0.2)
    open_discord()
    join_guild()
    join_channel()
    start_stream()
    return "stream started"

@app.route("/pause")
def pause():
    player.pause()
    return "Paused video"

@app.route("/play")
def play():
    player.play()
    return "Resumed video"

def locateOnScreen(image):
    location = pyautogui.locateOnScreen(image, grayscale=True, confidence=.7)
    if location == None:
        raise Exception("Image not found: " + image)
    return location

def get_guild_location():
    try:
        return locateOnScreen("assets/guild.png")
    except Exception as e:
        return locateOnScreen("assets/guild_selected.png")

def get_channel_location():
    return locateOnScreen("assets/channel.png")

def get_stream_button_location():
    return locateOnScreen("assets/stream_button.png")

def get_discord_share_stream_location():
    return locateOnScreen("assets/discord_share_screen.png")

def get_stream_location():
    try:
        return locateOnScreen("assets/stream.png")
    except Exception as e:
        return None

def get_go_live_location():
    return locateOnScreen("assets/go_live.png")

def open_discord():
    print("Opening Discord")
    pyautogui.getWindowsWithTitle("discord")[0].minimize()
    sleep(0.2)
    pyautogui.getWindowsWithTitle("discord")[0].maximize()
    sleep(0.5)
    
def join_guild():
    print("Joining guild")
    pyautogui.moveTo(get_guild_location())
    pyautogui.click()
    sleep(0.4)

def join_channel():
    print("Joining channel")
    pyautogui.moveTo(get_channel_location())
    pyautogui.click()
    sleep(0.2)
    
def start_stream():
    print("Starting stream")
    pyautogui.moveTo(get_stream_button_location())
    pyautogui.click()
    sleep(2)
    player.play()
    sleep(0.1)
    player.pause()
    pyautogui.moveTo(get_discord_share_stream_location())
    pyautogui.click()
    sleep(0.2)
    while get_stream_location() == None:
        # send the windows tab key to switch to the stream window
        pyautogui.press("tab")
        sleep(0.5)
    pyautogui.moveTo(get_stream_location())
    pyautogui.click()
    sleep(0.2)
    pyautogui.moveTo(get_go_live_location())
    pyautogui.click()
    player.set_fullscreen(True)
    player.play()
    