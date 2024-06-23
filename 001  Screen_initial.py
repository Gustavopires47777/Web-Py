from tkinter import *

root = Tk() #Root evoca tela

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop() #Loop para manter tela ativa
    def tela(self):
        self.root.title("Exemplo aplicativo")
        self.root.configure(background ='#871F78')
        self.root.geometry("786x588")
        self.root.resizable(True,True) #Responsive shell

Application()
 
