import tkinter as tk
from tkinter import ttk
import Object as obj
import Simulation as sim

# GUI window main application

# variable to keep track of new simulations default name extension
sim_increment = 0
class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        

        # Frame for object creation, manipulation, and display [right side of Canvas]
        # self.object_selection_frame = tk.Frame(root).pack(side="top")
        #self.add_object_entry_frame = tk.Entry(self.object_selection_frame, textvariable=self.new_obj_name, text="Enter Object Name").pack(side="bottom")
        #self.object_creation_button = tk.Button(self.object_selection_frame, bg="BLUE", text="Add Object", command=self.add_object).pack(side="top")
        #self.object_display = tk.Label(self.object_selection_frame, text=self.objects[0]).pack(side="top")

        # Frame for creating a new simulation [top]
        self.create_simulation_frame = tk.Frame(root).pack(side="top")
        self.create_simulation_button = tk.Button(self.create_simulation_frame, text="NEW SIMULATION", command=self.new_simulation).pack()


        # Canvas for simulation
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="top", fill="both", expand=False)
        
        self.simulations = {}
        self.current_simulation = ''

        
    def new_simulation(self, name=("%s%s" % ('sim_', sim_increment+1)), width=100, height=100):
        sim_increment = sim_increment + 1
        # delete old canvas data
        self.canvas.delete("all")

        # delete old simulation data
        #### clear vectors, etc.

        # resize canvas and set params
        self.canvas.config(width=width, height=height, bg="lightgrey", highlightthickness=5, highlightbackground="dodger blue")

        self.simulations[name] = sim.Simulation(root, self.c)

    def select_simulation(self, name):
        self.current_simulation = self.simulations[name]
        # error check



        




        

        
        

            






if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500,500)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()