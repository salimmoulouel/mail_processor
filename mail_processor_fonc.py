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


imapObj = imapclient.IMAPClient('outlook.office365.com', ssl=True)
imapObj.login('salimmouloueletude@outlook.fr', 'Smoul25082015')
import pdb;pdb.set_trace()
imapObj.select_folder('INBOX', readonly=True)
import pdb;pdb.set_trace()
UIDs = imapObj.search('SEEN')
i=1        
def calculate(*args):
    try:
        print("izan")
        global i
        rawMessages = imapObj.fetch(UIDs[i], [b'BODY[]'])
        ms_k=next(iter(rawMessages.keys()))
        #import pdb;pdb.set_trace()
        
        coded_message=rawMessages[ms_k][b'BODY[]']
        #import pdb;pdb.set_trace()
        
        message = pyzmail.PyzMessage.factory(coded_message)
        
        #import pdb;pdb.set_trace()
        if message.html_part != None:
            contenu_message=message.html_part.get_payload().decode(message.html_part.charset)
        else:   
            contenu_message=message.text_part.get_payload().decode(message.text_part.charset)
        
#        meters.set(contenu_message)
        T.delete("0.0",END)
        T.insert("0.0", contenu_message)
        print(contenu_message)
        i+=1
        
    except ValueError:
        pass
    
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=30, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

T = Text(root, height=20)
T.grid(columnspan=2, row=1, sticky=(W,E))
#import pdb;pdb.set_trace()
ttk.Scrollbar(T)

#meters = StringVar()

#ttk.Scrollbar(meters)

#T = 
#ttk.Label(mainframe, textvariable=meters).grid(columnspan=2, row=1, sticky=(W,E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)
i+=1
root.mainloop()




#except ConnectionResetError