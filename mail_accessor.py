
import os
import re
import tkinter as tk
from tkinter import messagebox
import webbrowser
import imapclient
from imapclient.exceptions import LoginError
from socket import gaierror
import pyzmail
import smtplib
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
            
            self.imapObj = imapclient.IMAPClient(self.settings.serveurs_imap[self.settings.choosed_serveur.get()], ssl=True)
            #import pdb;pdb.set_trace()
            retour = self.imapObj.login(self.settings.email.get(), self.settings.mdp.get())
            messagebox.showinfo("sucess", retour)
            self._show_folders()
            #mise en place partie smtp
            self.smtpObj = smtplib.SMTP(self.settings.serveurs_smtp[self.settings.choosed_serveur.get()], 587)
            
            self.smtpObj.ehlo()
            self.smtpObj.starttls()

            self.smtpObj.login(self.settings.email.get(), self.settings.mdp.get())
        except gaierror as e:
            #erreur de serveur
            messagebox.showinfo("connection error", "veuillez mettre un nom de serveur imap correct")

        except LoginError as e:
            # erreur de login ou mdp
            messagebox.showinfo("connection error", "login ou mot de passe incorrect")
            
    def _show_folders(self):
        """show a list of folders present inside the root folder of the mail box"""
        folders_list =self._list_folders()
        #self.settings.root_folders_list.delete(0,'end')
        self.settings.root_folders_list.insert(0, *folders_list) 
    
    def _list_folders(self):
        """ get the list of folders inside the root mail box dir"""
        folders_list = self.imapObj.list_folders()
        folders_list = [folder[-1] for folder in folders_list]
        return folders_list
    
    
    
        
    def show_root_folder_content(self,event):
        self.settings.choosed_root_folder = self.settings.root_folders_list.get(self.settings.root_folders_list.curselection())       
        #import pdb;pdb.set_trace()
        sub_folders_list=self.imapObj.select_folder(self.settings.choosed_root_folder, readonly=True)
        #import pdb;pdb.set_trace()
        sub_folders_list=list(sub_folders_list[b'FLAGS'])
        #import pdb;pdb.set_trace()
        
        sub_folders_list=[mot.decode().lstrip("\\") for mot in sub_folders_list]
        self.settings.sub_root_folders_list.delete(0,"end")
        #import pdb;pdb.set_trace()
        self.settings.sub_root_folders_list.insert(0, *sub_folders_list) 
        #import pdb;pdb.set_trace()
        
        #if (disconnected):
            #reconnect
        #try interact
        #catch reconnect
        
    
    def get_mails_from_folder(self,event=None):
        self.settings.choosed_sub_folder = self.settings.sub_root_folders_list.get(self.settings.sub_root_folders_list.curselection())       
        
        #import pdb;pdb.set_trace()
        self.UIDs=self.imapObj.search(self.settings.choosed_sub_folder)
        #import pdb;pdb.set_trace()
        self.settings.id_mail=0
        self.mail_header()
    
    def mail_header(self):
        self.settings.mails_list.delete(0,"end")

        for message in self.UIDs[self.settings.id_mail:self.settings.id_mail+10]:
            #import pdb;pdb.set_trace()
            rawMessage = self.imapObj.fetch(message, [b'BODY[]',b'FLAGS'])
            message_content=pyzmail.PyzMessage.factory(rawMessage[message][b'BODY[]'])
            
            sujet=message_content.get_subject()
            de=message_content.get_addresses('from')
            
            date_mail=message_content.get_all("date")
            #import pdb;pdb.set_trace()
            
            head_mail="   ".join([em[1] for em in de])+date_mail[0]+"   "+ sujet+ "UID : "+str(message)
            
            self.settings.mails_list.insert("end",head_mail)
            #message = pyzmail.PyzMessage.factory(coded_message)
            
    def show_mail(self,event):
        self.settings.choosed_mail = self.settings.mails_list.get(self.settings.mails_list.curselection())   
        uid_getter=re.compile("(UID : )(\d+)")
        self.settings.choosed_mail=int(uid_getter.findall(self.settings.choosed_mail)[0][1])
        
        rawMessage = self.imapObj.fetch(self.settings.choosed_mail, [b'BODY[]',b'FLAGS'])
        message=pyzmail.PyzMessage.factory(rawMessage[self.settings.choosed_mail][b'BODY[]'])
        if message.html_part != None:
            contenu_message=message.html_part.get_payload().decode(message.html_part.charset)
            with open("html_renderer.html", 'w') as f:
                f.write(contenu_message)
            webbrowser.open(os.path.join(".","html_renderer.html"))
        else:   
            contenu_message=message.text_part.get_payload().decode(message.text_part.charset)
        self.program.window.text_mail.delete(1.0,"end")    
        self.program.window.text_mail.insert(1.0,contenu_message)
        self.settings.mail_sender=[mail[1] for mail in message.get_addresses('from')]
        
        #import pdb;pdb.set_trace()
        
        
        
        #self.program.window.text_mail.set_content("""<html><body><h1>Hello world!</h1><body><html>""")
    def send_pos_response(self):
        #import pdb;pdb.set_trace()
        positif_mail='''Subject: reponse candidature'...\n
        ... Nous sommmes interesse, etes vous disponibles '''
        self.smtpObj.sendmail(self.settings.email.get(),self.settings.mail_sender[0],positif_mail.encode("ascii")) 
        
        
    def send_neg_response(self):
        #import pdb;pdb.set_trace()
        positif_mail='''Subject: reponse candidature'...\n
        .. desole votre candidature ne nous interesse pas  '''
        self.smtpObj.sendmail(self.settings.email.get(),self.settings.mail_sender[0],positif_mail) 
    
    def get_next(self,):
        self.settings.id_mail+=10
        self.mail_header()
    def get_prev(self):
        self.settings.id_mail-=10
        self.mail_header()
            
