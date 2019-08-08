import os
from bs4 import BeautifulSoup
# The built in package for RegEx
import re
from urllib.request import urlopen


# TODO make it arguments to be passed in
# Gets the directory in which to save the videos
def getSavDir():
    global saveDir
    saveDir = input("The directory in which to store the videos: ")

# TODO make it as command line arguments
# Gets the name of the channel to save videos from
def getChannel():
    global channel
    channel = input("The channel from which to save: ")


# Here for now for ease of access
# The second line is the playlist to download
command = 'youtube-dl\
        https://www.youtube.com/playlist?list=PL9fPq3eQfaaD0cf5c7wkzMoj2kifzGO4U\
        -i -w --write-info-json'


def main():
    getSavDir()
    getChannel()
    print(channel, " saving in ", saveDir)
    print("youtube-dl --help")
    os.system("youtube-dl --help")

main()
