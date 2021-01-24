from tkinter import *
from tkinter import ttk
import pyzmail
import imapclient
import pprint

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass



#instantiation de la fenetre 
root = Tk()
root.title("Feet to Meters")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#instantion d'une fenetre principale sur la fenetre
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


#separation de l'ecran en 2 colonnes
mainframe.grid_columnconfigure(0, weight=1, uniform="group1")
mainframe.grid_columnconfigure(1, weight=1, uniform="group1")

mainframe.grid_rowconfigure(0, weight=1 )
#instantiation de la fenetre de gauche qui contiendra les boutons
left_side= ttk.Frame(mainframe)
left_side.grid(row=0,column=0, sticky=(N,S,E,W))
left_side.columnconfigure(0, weight=1)
left_side.rowconfigure(0, weight=1)
#instantiation de la fenetre de droite qui contiendra le text et quelque fonctinnalités
right_side= ttk.Frame(mainframe)
right_side.grid(row=0,column=1, sticky=(N,S,E,W))
right_side.grid_rowconfigure(0, weight=5,uniform="group1")
right_side.grid_rowconfigure(1, weight=2,uniform="group1")

right_side.columnconfigure(0, weight=1)


#instantiation du text de la fenetre de droite
T = Text(right_side)
T.grid(row=0,column=0, sticky="news")#le text prend tout la fenetre (scroll bar sera ajouté automatiquement à coté)

#instantiation de la barre glissante
S=ttk.Scrollbar(right_side,command=T.yview, orient="vertical")
S.grid(row=0,column=1,sticky="ns")#mettre row 0 pour que la barre soit sur la meme ligne que le texte et column 1 pour qu'elle soit à droite
f1 = ttk.Frame(right_side)
f1.grid(row=1, sticky="nsew")


root.mainloop()




#except ConnectionResetError