#!/usr/bin/env python

from pytube import YouTube
import argparse
import os

HOME = os.path.expanduser('~')
VIDEO_DIR = os.path.join(HOME,'Videos')
AUDIO_DIR = os.path.join(HOME,'Audio')

def download(videoUrl):
    video = YouTube(videoUrl)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_DIR)
    except:
        print('Failed to download video')

    print('video was downloaded successfully')

def download_audio(videoUrl):
    video = YouTube(videoUrl)
    audio = video.streams.filter(only_audio=True).first()

    try:
        audio.download(AUDIO_DIR)
    except:
        print('Failed to download audio')

    print('audio was downloaded successfully')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', '--video', required=True, help = 'URL to youtube video')
    ap.add_argument('-a', '--audio', required = False, help = 'audio only', action = argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())

    if args['audio']:
        #download audio
        download_audio(args['video'])
    else:
        #download video
        download(args['video'])
