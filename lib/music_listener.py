class MusicListener:
    def __init__(self):
        self.track_list = []

    def add(self, track):
        if track == '':
            pass
        else:
            self.track_list.append(track)
        
    def return_track_list(self):
        return f"Track list: {self.track_list}"
    
    