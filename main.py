import tkinter as tk
from tkinter import ttk
import Object as obj
import Simulation as sim

# GUI window main application


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # variable to keep track of new simulations default name extension
        self.sim_increment = '0'

        # Frame for object creation, manipulation, and display [right side of Canvas]
        # self.object_selection_frame = tk.Frame(root).pack(side="top")
        #self.add_object_entry_frame = tk.Entry(self.object_selection_frame, textvariable=self.new_obj_name, text="Enter Object Name").pack(side="bottom")
        #self.object_creation_button = tk.Button(self.object_selection_frame, bg="BLUE", text="Add Object", command=self.add_object).pack(side="top")
        #self.object_display = tk.Label(self.object_selection_frame, text=self.objects[0]).pack(side="top")

        # Frame for creating a new simulation [top]
        self.create_simulation_frame = tk.Frame(root).pack(side="top")
        self.create_simulation_button = tk.Button(self.create_simulation_frame, text="NEW SIMULATION", command=self.create_simulation_input).pack()

        self.simulations = {}
        self.current_simulation = "Current Simulation Defualt Title"

        #Frame for simulation room
        self.simulation_room = tk.Frame(root).pack(side="top")
        self.simulation_label = tk.Label(self.simulation_room, text=self.current_simulation).pack(side="top")


        #### create grid for canvas and selection pane####
        # Canvas for simulation
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="top", fill="both", expand=False)
    


    def create_simulation_input(self):
        input_label = tk.Label(self.create_simulation_frame, text="Name").pack(side="top")
        name_entry = tk.StringVar()
        name_entry_widget = tk.Entry(self.create_simulation_frame, textvariable=name_entry).pack(side="top")
        #add check to make sure something was input
        create_button = tk.Button(self.create_simulation_frame, text="Create Simulation", command=self.new_simulation(name=name_entry.get())).pack(side="top")
    
    # def create_simulation_submit(self, sim_name):
    #     self.new_simulation(name=sim_name)



    def new_simulation(self, name="sim", w=500, h=500):
        self.simulations[name] = sim.Simulation(root, self.canvas, name)
        #####check for repeat names and throw error
        print(self.simulations)
        self.current_simulation = name
        print(self.current_simulation)

        # if(name == "sim"):
        #     name = name + self.sim_increment
        #     self.sim_increment+=1

        # delete old canvas data
        self.canvas.delete("all")

        # delete old simulation data
        #### clear vectors, etc.

        # resize canvas and set params
        self.canvas.config(width=w, height=h, bg="lightgrey", highlightthickness=3, highlightbackground='#000000')

        #self.simulations[name] = sim.Simulation(root, self.c)

    def select_simulation(self, name):
        self.current_simulation = name
        print(self.current_simulation)
        # error check
        




        




        

        
        

            






if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500,500)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()