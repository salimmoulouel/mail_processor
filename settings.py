import tkinter as tk


class Settings:
    """class contain general settings of the application"""
    def __init__(self):
        self.serveurs={"Outlook":"outlook.office365.com","Gmail":"imap.gmail.com"}
        self.choosed_serveur = None
        self.email = None
        self.mdp= None
        