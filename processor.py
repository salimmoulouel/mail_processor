
from settings import Settings
import windows as wd
class Processor:
    def __init__(self):
        self.settings=Settings()
        self.window=wd.Window(self)
        
    def launch(self):
        """launch the program"""
        self.window.launch()
        
        self.mail_acessor=None
        
if __name__ == "__main__" :
    program=Processor()
    program.launch()     
    
    
from mail_accessor import Mail_Accessor
            
            
            
    


