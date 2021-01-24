import imapclient
class Mail_Accessor:
    def __init__(self,processor):
        self.program=processor
        self._init_connection(imap_serveur=processor)
    
    
    
    def _init_connection(self,imap_serveur='outlook.office365.com',login='salimmouloueletude@outlook.fr',mdp='Smoul25082015'):
        self.imapObj = imapclient.IMAPClient(imap_serveur, ssl=True)
        self.imapObj.login(login, mdp)
            
        

    def _list_folders(self):
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