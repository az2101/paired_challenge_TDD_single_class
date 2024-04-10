# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
_

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicListener:
  

    def __init__(self):
        self.track_list = []

    def add(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds the track to the track list
        pass # No code here yet

    def return_track_list(self):
        # Returns:
        #   A list of added tracks
        # starting with 'Track list:'
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given an empty string
Does not get added to list
"""
music_listener = MusicListener()
music_listener.add('') => []
"""
Given a track
Adds track to track list
"""
music_listener = MusicListener()
music_listener.add('Track 1') => ['Track 1']

"""
Given multiple tracks
Appends all to list
"""
music_listener = MusicListener()
music_listener.add('Track 1')
music_listener.add('Track 2')
music_listener.add('Track 3') => ['Track 1', 'Track 2', 'Track 3']

"""
#return_track_list 
returns a list of tracks added
"""
music_listener = MusicListener()
music_listener.add('Track 1')
music_listener.add('Track 2')
music_listener.add('Track 3')
music_listener.return_track_list() => 'Track list: ['Track 1', 'Track 2', 'Track 3']'


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
