# Library Here -> https://pytube.io/en/latest/

# TODO How to choose download quality (from ???-4k)
# TODO Run on windows[X] and macos[]
# TODO Add exception blocks for downloaded video
# Video already downloaded[]
#
# TODO See if You can download audio and not video

# Checa if video has already been downloaded
# if yt.title==:
#    print("There is already a video with that name. Cannot download video")

# Libraries to get YouTube video and users' Downloads folder path
from pytube import YouTube
from pathlib import Path
import time
import os

download_path = str(Path.home() / "Downloads")


def main():
    print("Hello and welcome to YtDownloader! :)")
    getUrl()


def getUrl():
    # Gets video URL from user
    url = None

    # TODO add script if a URL isn't provided (close but can still break if input is just http:/)
    url = input(
        'Please input a valid video URL "https://www.youtube.com/..."\n')
    if url == None:
        getUrl()

    # Creates YouTube object and assigns users' Downloads folder path
    video = YouTube(url)

    # Prints video data
    print("Video Title: ", video.title)
    print("Views: ", video.views)
    chooseDownload(video)


def chooseDownload(video):
    c = input('Press [V] for video and audio. Or [A] for audio only\n')
    # Video and audio
    if (c.lower() == 'v'):
        videoAndAudio(video)

    # Audio only
    elif (c.lower() == 'a'):
        audioOnly(video)

    # Incorrect input
    else:
        chooseDownload()


def videoAndAudio(video):
    print("DOWNLOADING...\n")
    # Gets highest quality video (up to 720 as of now) and then downloads it
    fullVideo = video.streams.get_highest_resolution()
    fullVideo.download(download_path)

    print("Video has been downloaded successfully!")
    anotherVideo()


def audioOnly(video):
    print("DOWNLOADING...\n" "This may take a while :)")
    audio = video.streams.get_audio_only()

    # New code
    audioOut = audio.download(download_path)
    base, ext = os.path.splitext(audioOut)
    new_file = base + '.wav'
    os.rename(audioOut, new_file)
    # End of new code
    print("Audio has been downloaded successfully!")
    anotherVideo()


def anotherVideo():
    a = input('Would you like to download another video? (Y/N)\n')

    # User wants to download another
    if (a.lower() == 'y'):
        getUrl()

    # User doesn't want to download another
    elif (a.lower() == 'n'):
        closeProgram()

    # Incorrect input
    else:
        anotherVideo()


def closeProgram():
    print('Thank you for using YtDownloader!')
    print('It will automatically close in 10 seconds.')
    time.sleep(10)


main()
