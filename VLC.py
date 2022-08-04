from vlc import Instance
import time
import os
os.add_dll_directory(os.getcwd())


class VLC:
    def __init__(self):
        self.Player = Instance('--loop --reset-config --reset-plugins-cache')

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        path = r"C:\Users\Bastianh\CinePlex\videos"
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()