
import tkinter as tk


class Settings:
    """class contain general settings of the application"""
    def __init__(self):
        self.serveurs_imap={"Outlook":"outlook.office365.com","Gmail":"imap.gmail.com"}
        self.serveurs_smtp={"Outlook":"SMTP.office365.com","Gmail":"smtp.gmail.com"}
        self.choosed_serveur = None
        self.email = None
        self.mdp= None
        self.root_folders_list = None
        self.choosed_root_folder = None
        self.sub_root_folders_list = None
        self.choosed_sub_folder = None
        self.mails_list = None
        self.mail_sender = None
        self.id_mail = None