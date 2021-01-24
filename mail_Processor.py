import tkinter as tk

def init_connection():
    imapObj = imapclient.IMAPClient('outlook.office365.com', ssl=True)
    imapObj.login('salimmouloueletude@outlook.fr', 'Smoul25082015')
        
        

def _list_folders():
    folders_list = imapObj.list_folders()
    folders_list = [folder[-1] for folder in folders_list]
    return folders_list
def check_mails():
    folders_list=_list_folders()
    folders_list_str="\n".join(folders_list)
    rep_valid=False
    while (not rep_valid):
        response = input(""" choose one of thoose folders""" + str(folders_list_str))
        if response in folders_list:
            rep_valid=True
    
    imapObj.select_folder(response, readonly=True)
    UIDs = imapObj.search('SEEN')
        

def 