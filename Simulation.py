import tkinter as tk
from tkinter import Canvas
import Object as obj

OBJ_DIAM = 10

class Simulation():

    def __init__(self, parent, _canvas):
        
        self.parent = parent
        self.canvas = _canvas
        self.size = (self.canvas.winfo_width() , self.canvas.winfo_height())
        print("Simulation created with size", self.size)

        # Dictionary to store all Objects in the simulation
        self.objects = {}
        
        # Dictionary to store audio files in the simulation
        self.audios = {}
    
    def add_object(self, name, x, y):
        self.objects[name] = obj.Object(name, x, y)
        print(name, " added to simulation with pos=", self.objects[name].pos)
        self.canvas.create_oval(x,y,x+OBJ_DIAM, y+ OBJ_DIAM)
        


