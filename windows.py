import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self):
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

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        #instantion d'une fenetre principale sur la fenetre
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky="nsew")


        #separation de l'ecran en 2 colonnes
        self.mainframe.grid_columnconfigure(0, weight=1, uniform="group1")
        self.mainframe.grid_columnconfigure(1, weight=1, uniform="group1")

        
    def _left_side_instantiate(self):
        """ instantiation of the left side of main window"""
         #instantiation de la fenetre de gauche qui contiendra les boutons
        self.left_side= ttk.Frame(self.mainframe)
        self.left_side.grid(row=0,column=0, sticky="nsew")
        #self.left_side.columnconfigure(0, weight=1)
        #self.left_side.rowconfigure(0, weight=1)
        
        ttk.Label(self.left_side, text="choisisez le serveur de messagerie").grid(column=0, row=0, sticky="nw")
        serveur_choices = ['Outlook', 'Gmail']
        self.choosed_serveur = tk.StringVar()
        self.choosed_serveur.set('GB')
        
        ttk.Label(self.left_side, text="adresse e-mail").grid(row=1,column=0, sticky="nw")
        
        ttk.Label(self.left_side, text="mot de passe").grid(row=2,column=0,  sticky="nw")
        
        

        tk.OptionMenu(self.left_side, self.choosed_serveur, *serveur_choices).grid(row=0,column=1,sticky="n")
    def _right_side_instantiate(self):
        """ instantiation of the right side of main window"""
        self.right_side= ttk.Frame(self.mainframe)
        self.right_side.grid(row=0,column=1, sticky="nsew")
        self.right_side.grid_rowconfigure(0, weight=5,uniform="group1")
        self.right_side.grid_rowconfigure(1, weight=2,uniform="group1")
        
        
        #instantiation du text de la fenetre de droite
        self.text_mail = tk.Text(self.right_side)
        self.text_mail.grid(row=0,column=0, sticky="news")#le text prend tout la fenetre (scroll bar sera ajouté automatiquement à coté)

        #instantiation de la barre glissante
        self.S=ttk.Scrollbar(self.right_side,command=self.text_mail, orient="vertical")
        self.S.grid(row=0,column=1,sticky="ns")#mettre row 0 pour que la barre soit sur la meme ligne que le texte et column 1 pour qu'elle soit à droite
        
        self.boutons_mail = ttk.Frame(self.right_side)
        self.boutons_mail.grid(row=1, sticky="nsew")
    
    
    
        
    def launch(self):
        self.root.mainloop()