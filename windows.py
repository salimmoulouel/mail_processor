
from processor import Processor
from settings import Settings
import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self,processor : Processor):
        self.program=processor
        self.settings= self.program.settings
        self._instantiate_screen()
        
        
    def _instantiate_screen(self):
        """instantiation of the screen"""
        self._main_window_instantiate()
        self._right_side_instantiate()
        self._left_side_instantiate()
       
        
    
    def _main_window_instantiate(self):
        """ instantiation of the main window with splitting of the windows to two columns"""
        #instantiation de la fenetre 
        self.root = tk.Tk()
        self.root.title("Feet to Meters")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        #instantion d'une fenetre principale sur la fenetre
        self.mainframe = ttk.Frame(self.root, padding="1 1 4 4")
        self.mainframe.grid(column=0, row=0, sticky="nsew")


        #separation de l'ecran en 2 colonnes
        self.mainframe.grid_columnconfigure(0, weight=1, uniform="group1")
        self.mainframe.grid_columnconfigure(1, weight=1, uniform="group1")

        self.mainframe.grid_rowconfigure(0, weight=1)
        #self.mainframe.grid_rowconfigure(0, weight=1, uniform="group1")

        
    def _left_side_instantiate(self):
        """ instantiation of the left side of main window"""
         #instantiation de la fenetre de gauche qui contiendra les boutons
        self.left_side= ttk.Frame(self.mainframe)
        self.left_side.grid(row=0,column=0, sticky="nsew")

        self.left_side.grid_columnconfigure(0,weight=2,uniform="group1")
        self.left_side.grid_columnconfigure(1,weight=2,uniform="group1")

        self._information_serveur_instantiate()    
        
        
    def _information_serveur_instantiate(self):
        """instantiate widgets for serveur information outpout"""
        ttk.Label(self.left_side, text="choisisez le serveur de messagerie",anchor="center").grid(column=0, row=0, sticky="nsew")
        serveur_choices = list(self.settings.serveurs.keys())
        self.settings.choosed_serveur = tk.StringVar()
        self.settings.choosed_serveur.set('Outlook')
        tk.OptionMenu(self.left_side, self.settings.choosed_serveur, *serveur_choices).grid(row=0,column=1,sticky="nsew")
        
        ttk.Label(self.left_side, text="adresse e-mail",anchor="center").grid(row=1,column=0, sticky="nsew")
        self.settings.email = tk.StringVar()
        self.settings.email.set("salimmouloueletude@outlook.fr")
        feet_entry = ttk.Entry(self.left_side, textvariable=self.settings.email,width=50)
        feet_entry.grid(row=1, column=1,  sticky="nsew")

        ttk.Label(self.left_side, text="mot de passe", anchor="center").grid(row=2,column=0,  sticky="nsew")
        self.settings.mdp = tk.StringVar()
        self.settings.mdp.set("Smoul25082015")

        feet_entry = ttk.Entry(self.left_side, textvariable=self.settings.mdp,width=50)
        feet_entry.grid(row=2, column=1,  sticky="nsew")
        
        ttk.Button(self.left_side, text="Connect", command=self.program.mail_acessor.init_connection).grid(column=1, row=3, sticky="nsew")
        feet_entry.grid(row=2, column=1,  sticky="nsew")
        
        ttk.Label(self.left_side, text="list des dossiers",anchor="center").grid(row=4,column=0,pady=5,sticky="nsew")
        self.settings.root_folders_list=tk.Listbox(self.left_side)
        self.settings.root_folders_list.grid(row=4,column=1,pady=5,sticky="nsew")
        self.settings.root_folders_list.bind('<ButtonRelease-1>', self.program.mail_acessor.show_root_folder_content)

        ttk.Label(self.left_side, text="list des sous dossiers",anchor="center").grid(row=5,column=0,pady=5,sticky="nsew")
        self.settings.sub_root_folders_list=tk.Listbox(self.left_side)
        self.settings.sub_root_folders_list.grid(row=5,column=1,pady=5,sticky="nsew")
        
    
    def _right_side_instantiate(self):
        """ instantiation of the right side of main window"""
        self.right_side= ttk.Frame(self.mainframe)
        self.right_side.grid(row=0,column=1, sticky="nsew")
        self.right_side.grid_columnconfigure(0, weight=1,uniform="group1")
        self.right_side.grid_rowconfigure(0, weight=7,uniform="g1")
        self.right_side.grid_rowconfigure(1, weight=3,uniform="g1")
        
        
        #instantiation du text de la fenetre de droite
        self.text_mail = tk.Text(self.right_side)
        self.text_mail.grid(row=0,column=0, sticky="nsew")#le text prend tout la fenetre (scroll bar sera ajouté automatiquement à coté)

        #instantiation de la barre glissante
        self.S=ttk.Scrollbar(self.right_side,command=self.text_mail, orient="vertical")
        self.S.grid(row=0,column=1,sticky="nsw")#mettre row 0 pour que la barre soit sur la meme ligne que le texte et column 1 pour qu'elle soit à droite
        
        self.boutons_mail = ttk.Frame(self.right_side)
        self.boutons_mail.grid(row=1, sticky="nsew")
    
    
    
    def _connect(self):
        """ when connection button pressed"""
        self.program.mail_acessor=Mail_Accessor(self.program)
        
    def launch(self):
        """launch the tinker window"""
        self.root.mainloop()
        
from mail_accessor import Mail_Accessor