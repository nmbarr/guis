import customtkinter as ctk

class HeaderBox(ctk.CTkFrame):
    def __init__(self, master, width, height, fg_color, border_color):
        super().__init__(master)

        self.width = width
        self.height = height
        self.fg_color = fg_color
        self.border_color = border_color

        self.header_box = ctk.CTkFrame(self, width=self.width, height=self.height, fg_color=self.fg_color, border_color=self.border_color)
        self.header_box.pack(fill="both", expand=True)
