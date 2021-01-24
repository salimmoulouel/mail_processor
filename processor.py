from mail_accessor import Mail_Accessor
import windows as wd
class Processor:
    def __init__(self):
        self.window=wd.Window()
        
    def launch(self):
        self.window.launch()
        self.mail_acessor=Mail_Accessor(self)
if __name__ == "__main__" :
    program=Processor()
    program.launch()     
            
            
            
    


