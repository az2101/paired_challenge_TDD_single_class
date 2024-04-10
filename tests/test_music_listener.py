
from lib.music_listener import *

"""
Given an empty string
Does not get added to list
"""

def test_empty_string_not_added():
    music_listener = MusicListener()
    music_listener.add('')
    assert music_listener.return_track_list() == "Track list: []"
"""
Given a track
Adds track to track list
"""
def test_track_is_added():
    music_listener = MusicListener()
    music_listener.add('Track 1')
    assert music_listener.return_track_list() == "Track list: ['Track 1']"


"""
Given multiple tracks
Appends all to list
"""
def test_multiple_tracks_are_added():
    music_listener = MusicListener()
    music_listener.add('Track 1')
    music_listener.add('Track 2')
    music_listener.add('')
    music_listener.add('Track 3')
    assert music_listener.return_track_list() == "Track list: ['Track 1', 'Track 2', 'Track 3']"

"""
#return_track_list 
returns a list of tracks added
"""
def test_track_list_returned():
    music_listener = MusicListener()
    music_listener.add('Track 1')
    music_listener.add('Track 2')
    music_listener.add('')
    music_listener.add('Track 3')
    assert music_listener.return_track_list() == "Track list: ['Track 1', 'Track 2', 'Track 3']"
