import customtkinter as ctk

class GUIButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(command=self.set_command)

    def set_command(self, command):
        self.configure(command=command)

    # If the 'Quit' button is clicked, close the GUI
    def generate_calibration_sheets(self):
        self.configure(command=self.quit)
