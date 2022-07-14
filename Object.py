import tkinter as tk


class Object():

    # class members
    def __init__(self, object_name, x_pos_start, y_pos_start):
        
        
        # class members
        self.object_name = object_name
        self.binded_audios = [] # maybe make a dictionary for audio_name and audio_object
        self.pos = (x_pos_start, y_pos_start)
        self.start_pos = (x_pos_start, y_pos_start)
    
    def bind_to(self, filename):
        self.binded_audios.append(filename)
    
    # returns current (x,y) coordinates as tuple
    def get_position(self):
        return self.pos
    
    # returns initialized (x,y) coordinates as tuple
    def get_start_pos(self):
        return self.start_pos
    
    # set current position to new location
    def move(self,x,y):
        pos = (x,y)
    
    
    