import tkinter as tk
from tkinter import messagebox
from processor import Processor
import imapclient
from imapclient.exceptions import LoginError
from socket import gaierror
class Mail_Accessor:
    """class that allow acess to mail"""
    def __init__(self,processor: Processor):
        self.program=processor
        self.settings=processor.settings
        
        self._init_connection(imap_serveur=self.settings.serveurs[self.settings.choosed_serveur.get()], login=self.settings.email.get(), mdp=self.settings.mdp.get())

    
    
    def _init_connection(self,imap_serveur='',login='',mdp=''):
        """initialise connection with the serveur"""
        try:
            self.imapObj = imapclient.IMAPClient(imap_serveur, ssl=True)
            #import pdb;pdb.set_trace()
            retour = self.imapObj.login(login, mdp)
            messagebox.showinfo("sucess", retour)
            folders_list =self._list_folders()
            #import pdb;pdb.set_trace()
            self.settings.root_folders_list.insert(0, *folders_list) 
        except gaierror as e:
            #erreur de serveur
            messagebox.showinfo("connection error", "veuillez mettre un nom de serveur imap correct")

        except LoginError as e:
            # erreur de login ou mdp
            messagebox.showinfo("connection error", "login ou mot de passe incorrect")
            
    def _list_folders(self):
        """ get the list of folders inside the root mail box dir"""
        folders_list = self.imapObj.list_folders()
        folders_list = [folder[-1] for folder in folders_list]
        return folders_list
    def check_mails(self):
        folders_list=self._list_folders()
        folders_list_str="\n".join(folders_list)
        rep_valid=False
        while (not rep_valid):
            response = input(""" choose one of thoose folders""" + str(folders_list_str))
            if response in folders_list:
                rep_valid=True
                
