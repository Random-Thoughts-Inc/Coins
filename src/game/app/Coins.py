# pylint: disable=line-too-long,unused-import,invalid-name
# type: ignore
"""
Coins Application
"""

import customtkinter as ctk


class Coins(ctk.CTk):
    """
    Coins Application
    """
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title("Coins")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets for the Coins Application
        """
        self.label = ctk.CTkLabel(self, text="Coins")
        self.label.grid(row=0, column=0, sticky="nsew")
