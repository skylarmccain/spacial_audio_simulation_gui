import tkinter as tk
from tkinter import ttk
import Object 

# GUI window main application
class MainApplication(tk.Frame):
    objects = []
    new_obj_name = tk.StringVar()

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Frame for object creation and selection
        self.object_selection_frame = tk.Frame(root).pack(side="top")
        self.add_object_entry_frame = tk.Entry(self.object_selection_frame, textvariable=self.new_obj_name, text="Enter Object Name").pack(side="bottom")
        self.object_creation_button = tk.Button(self.object_selection_frame, bg="BLUE", text="Add Object", command=self.add_object).pack(side="top")
        self.object_display = tk.Label(self.object_selection_frame, text=self.objects[0]).pack(side="top")
        

        
    def add_object(self):
        self.objects.append(Object(self.new_obj_name.get()))
        

            






if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500,500)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()