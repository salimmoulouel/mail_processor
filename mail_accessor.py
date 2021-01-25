
import tkinter as tk
from tkinter import messagebox
import imapclient
from imapclient.exceptions import LoginError
from socket import gaierror
class Mail_Accessor:
    """class that allow acess to mail"""
    def __init__(self,processor ):
        self.program=processor
        self.settings=processor.settings
        
        #self._init_connection(imap_serveur=self.settings.serveurs[self.settings.choosed_serveur.get()], login=self.settings.email.get(), mdp=self.settings.mdp.get())
        
    
    
    def init_connection(self):
        """initialise connection with the serveur"""
        try:
            #import pdb;pdb.set_trace()
            
            self.imapObj = imapclient.IMAPClient(self.settings.serveurs[self.settings.choosed_serveur.get()], ssl=True)
            #import pdb;pdb.set_trace()
            retour = self.imapObj.login(self.settings.email.get(), self.settings.mdp.get())
            messagebox.showinfo("sucess", retour)
            self._show_folders()
            
        except gaierror as e:
            #erreur de serveur
            messagebox.showinfo("connection error", "veuillez mettre un nom de serveur imap correct")

        except LoginError as e:
            # erreur de login ou mdp
            messagebox.showinfo("connection error", "login ou mot de passe incorrect")
            
    def _show_folders(self):
        """show a list of folders present inside the root folder of the mail box"""
        folders_list =self._list_folders()
        self.settings.root_folders_list.insert(0, *folders_list) 
    
    def _list_folders(self):
        """ get the list of folders inside the root mail box dir"""
        folders_list = self.imapObj.list_folders()
        folders_list = [folder[-1] for folder in folders_list]
        return folders_list
    
    
    
        
    def show_root_folder_content(self,event):
        self.settings.choosed_root_folder = self.settings.root_folders_list.get(self.settings.root_folders_list.curselection())       
        sub_folders_list=self.imapObj.select_folder(self.settings.choosed_root_folder, readonly=True)
        self.settings.sub_root_folders_list.insert(0, *sub_folders_list[b'FLAGS']) 
        import pdb;pdb.set_trace()
    
        #if (disconnected):
            #reconnect
        #try interact
        #catch reconnect
        
        
        
    def check_mails(self):
        folders_list=self._list_folders()
        folders_list_str="\n".join(folders_list)
        rep_valid=False
        while (not rep_valid):
            response = input(""" choose one of thoose folders""" + str(folders_list_str))
            if response in folders_list:
                rep_valid=True
                
