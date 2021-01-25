
from settings import Settings
import windows as wd

from mail_accessor import Mail_Accessor
class Processor:
    def __init__(self):
        self.settings=Settings()
        
        self.mail_acessor=Mail_Accessor(self)
        self.window=wd.Window(self)
        
        
    def launch(self):
        """launch the program"""
        
        self.window.launch()
        
        
        
if __name__ == "__main__" :
    program=Processor()
    program.launch()     
    
    
            
            
            
    


