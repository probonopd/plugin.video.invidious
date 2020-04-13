# encoding=utf8

# Debug with
# cat /storage/.kodi/temp/kodi.log

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
from urllib import urlencode
from urlparse import parse_qsl

import xbmcgui
import xbmcplugin
import xml.etree.ElementTree

from glob import glob
import json
from datetime import datetime

import urllib, json

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def list_videos(search_term):
    """
    Create the list of directories and/or playable videos in the Kodi interface.
    """

    xbmcplugin.setPluginCategory(_handle, search_term)
    xbmcplugin.setContent(_handle, 'videos')

    url = "https://invidious.snopyta.org/api/v1/search?q="+search_term+"&pretty=1&sort_by=upload_date"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    for video in data:
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html
        list_item = xbmcgui.ListItem(label=video["title"])
        list_item.setInfo('video', {'title': video["title"], 'mediatype': 'video'})
        list_item.setInfo('video', {'plot': video["description"]})
        list_item.setArt({'thumb': video["videoThumbnails"][4]["url"]}) # TODO: Select thumbnail with desired quality
        url = get_url(action='play', videoId=video["videoId"])
        list_item.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)


def play_video(videoId):
    """
    Play a video by the provided ID.
    """

    url = "https://invidious.snopyta.org/api/v1/videos/" + videoId
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    play_item = xbmcgui.ListItem(path=data["formatStreams"][0]["url"]) # TODO: Select stream with desired quality
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    """
    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'listing':
            list_videos(search_term=params['videoId'])
        elif params['action'] == 'play':
            play_video(params['videoId'])
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters
        search_term = "AppImage" # TODO: Get search terms from settings
        list_videos(search_term)


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
