from tkinter import *
from Vue.FrameDescription import FrameDescription
from Vue.FrameVisualisation import FrameVisualisation
from Vue.FrameEcranControle import FrameEcranControle
from Vue.FrameRL import FrameRL
from Vue.FrameHRL import FrameHRL
from Vue.FrameQMap import FrameQMap
from Vue.FrameHRL_final import FrameHRL_final

class FramePrincipale(Frame):
    
    def __init__(self, fenetre, env, agent, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.agent = agent
        self.env = env
        
        fenetre['bg']='white'

        #Frame de HRL
        #self.FrameHRL = FrameHRL(fenetre, self.env, self.agent, self)

<<<<<<< HEAD
        #Frame new
        #self.FrameHRL_new = FrameHRL_final(fenetre,self.env, self.agent, self)
=======
        #Frame HRL new
        self.FrameHRL_new = FrameHRL_final(fenetre,self.env, self.agent, self)
>>>>>>> 1a577202797fed7231e6ce5367e5a9cbd203a1b9

        # Frame de description
        #self.FrameDescription = FrameDescription(fenetre, self.env, self.agent, self)

        # Frame de visualisation
        self.FrameVisualisation = FrameVisualisation(fenetre, self.env, self.agent, self)

        # Ecran de controle
        self.FrameEcranControle = FrameEcranControle(fenetre, self.env, self.agent, self)

        # Frame d'apprentissage
        #self.FrameRL = FrameRL(fenetre, self.env, self.agent, self)

        # FrameQMAP
        self.FrameQMap = FrameQMap(fenetre, self.env, self.agent, self)