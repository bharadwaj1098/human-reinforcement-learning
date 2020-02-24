from tkinter import *
import os
from tkinter.messagebox import *
import numpy as np
from Modele.Environnement.Action import int2Action2String1Char
from Modele.Environnement.Action import int2Action2String
import matplotlib.pyplot as plt
from Modele.Environnement.Environnement import GoToTheGoalEnv2D
from Vue.FrameQMap import FrameQMap
import time as tm

class FrameHRL_final(Frame):
    
    def __init__(self, frame, env, agent, framePrincipale, **kwargs):
        self.agent = agent
        self.env = env
        self.framePrincipale = framePrincipale

        self.FrameHRL_new = LabelFrame(frame, text = "Renforcement Humain", bg="white", borderwidth=2, relief=GROOVE)
        self.FrameHRL_new.pack(side=TOP, padx=5, pady=5)

        self.FrameLoadW = LabelFrame(self.FrameHRL_new, text = "Charger des poids", bg="white", borderwidth=2, relief=GROOVE)
        self.FrameLoadW.pack(side=TOP, padx=2, pady=2)

        self.FrameTraining = LabelFrame(self.FrameHRL_new, text = "Lancer entrainement humain", bg="white", borderwidth=2, relief=GROOVE)
        self.FrameTraining.pack(side=TOP, padx=2, pady=2)

        self.FramePMActions = LabelFrame(self.FrameHRL_new, text = "Actions Prediction Map", bg="white", borderwidth=2, relief=GROOVE)
        self.FramePMActions.pack(side=TOP, padx=2, pady=2)

        self.FrameHumanAction = LabelFrame(self.FrameHRL_new, text = "Human Action", bg="white", borderwidth=2, relief=GROOVE)
        self.FrameHumanAction.config(width=150, height=150)
        self.FrameHumanAction.pack(side=TOP, padx=5, pady=5)

        self.var = DoubleVar()
        self.HumanActionButton1 = Button(self.FrameHumanAction, text='Oui', command=lambda: self.var.set(1))
        self.HumanActionButton2 = Button(self.FrameHumanAction, text='Non', command=lambda: self.var.set(2))
        self.HumanActionButton3 = Button(self.FrameHumanAction, text='JSP', command=lambda: self.var.set(3))
        # HumanActionButton.place(x=75,y=1)
        # HumanActionButton.place(x=75,y=5)
        # HumanActionButton.place(x=75,y=30)
        self.HumanActionButton1.grid(row=0, column=0, sticky="nsew",padx=5, pady=5)
        self.HumanActionButton2.grid(row=0, column=2, sticky="nsew",padx=5, pady=5)
        self.HumanActionButton3.grid(row=0, column=4, sticky="nsew",padx=5, pady=5)


        # self.FrameResetParam = LabelFrame(self.FrameHRL_new, text="Reset Parametres", bg="white", borderwidth=2,relief=GROOVE)
        # self.FrameResetParam.config(width=150, height=150)
        # self.FrameResetParam.pack(side=TOP, padx=5, pady=5)

        # self.ResetButton = Button(self.FrameResetParam, text='Reset Epsilon', command=self.resetAction)
        # self.ResetButton.pack()

        ## Lancer l'entrainement
        self.launchTrainingButton = Button(self.FrameTraining, text ="Lancer l'entrainement !!!", command=self.launchHRLAction)
        self.launchTrainingButton.pack()

        # self.FrameReplayLearningList = LabelFrame(self.FrameHRL_new, text = "Liste simulations", bg="white", borderwidth=2, relief=GROOVE)
        # self.FrameReplayLearningList.config(width=250, height=250)
        #self.FrameReplayLearningList.pack(side=TOP, padx=5, pady=5, expand=True) #, fill = BOTH)
        #self.FrameReplayLearningList.pack_propagate(0)

        ## ReplayLearningList
        # self.replayLearningList = Listbox(self.FrameReplayLearningList)
        # self.replayLearningList.pack(fill =BOTH)
        # self.replayLearningList.pack_propagate(0)
        # self.replayLearningList.bind('<<ListboxSelect>>', lambda evt: self.onselect(evt))

        # # Frame pour afficher Q valeur précédente
        # FrameQValuesAnt = LabelFrame(self.FrameHRL_new, text = "Q-values avant récompense humaine", bg="white", borderwidth=2, relief=GROOVE)
        # FrameQValuesAnt.pack(side=TOP, padx=5, pady=5)

        # # Frame pour afficher Q valeur après
        # FrameQValuesPost = LabelFrame(self.FrameHRL_new, text="Q-values après récompense humaine", bg="white", borderwidth=2,relief=GROOVE)
        # FrameQValuesPost.pack(side=BOTTOM, padx=5, pady=5)

        # # Frame Q valeur haut
        # FrameQHautAnt = LabelFrame(FrameQValuesAnt, text="Action Haute", bg="white", borderwidth=2,relief=GROOVE)
        # FrameQHautPost = LabelFrame(FrameQValuesPost, text="Action Haute", bg="white", borderwidth=2,relief=GROOVE)
        
        # # Frame Q valeur gauche
        # FrameQGaucheAnt = LabelFrame(FrameQValuesAnt, text="Action Gauche", bg="white", borderwidth=2, relief=GROOVE)
        # FrameQGauchePost = LabelFrame(FrameQValuesPost, text="Action Gauche", bg="white", borderwidth=2, relief=GROOVE)

        # # Frame Q valeur droite
        # FrameQDroiteAnt = LabelFrame(FrameQValuesAnt, text="Action Droite", bg="white", borderwidth=2, relief=GROOVE)
        # FrameQDroitePost = LabelFrame(FrameQValuesPost, text="Action Droite", bg="white", borderwidth=2, relief=GROOVE)

        # # Frame Q valeur bas
        # FrameQBasAnt = LabelFrame(FrameQValuesAnt, text="Action Bas", bg="white", borderwidth=2, relief=GROOVE)
        # FrameQBasPost = LabelFrame(FrameQValuesPost, text="Action Bas", bg="white", borderwidth=2, relief=GROOVE)

        # # Positionnement dans la grille
        # FrameQHautAnt.grid(row=0, column=1, sticky="nsew")
        # FrameQHautPost.grid(row=0, column=1, sticky="nsew")
        # FrameQGaucheAnt.grid(row=1, column=0, sticky="nsew")
        # FrameQGauchePost.grid(row=1, column=0, sticky="nsew")
        # FrameQDroiteAnt.grid(row=1, column=2, sticky="nsew")
        # FrameQDroitePost.grid(row=1, column=2, sticky="nsew")
        # FrameQBasAnt.grid(row=2, column=1, sticky="nsew")
        # FrameQBasPost.grid(row=2, column=1, sticky="nsew")

        # # StringVar pour récupérer les Qvalues
        # self.QHautAnt = StringVar()
        # self.QGaucheAnt = StringVar()
        # self.QDroiteAnt = StringVar()
        # self.QBasAnt = StringVar()
        # self.QHautPost = StringVar()
        # self.QGauchePost = StringVar()
        # self.QDroitePost = StringVar()
        # self.QBasPost = StringVar()
        

        # # Set Q values ant et post
        # self.QHautAnt.set(" Q Haut : ")
        # Label(FrameQHautAnt, textvariable=self.QHautAnt, bg="white", justify="left").pack()
        # self.QGaucheAnt.set(" Q Gauche : ")
        # Label(FrameQGaucheAnt, textvariable=self.QGaucheAnt, bg="white", justify="left").pack()
        # self.QDroiteAnt.set(" Q Droite : ")
        # Label(FrameQDroiteAnt, textvariable=self.QDroiteAnt, bg="white", justify="left").pack()
        # self.QBasAnt.set(" Q Bas : ")
        # Label(FrameQBasAnt, textvariable=self.QBasAnt, bg="white", justify="left").pack()
        # self.QHautPost.set(" Q Haut : ")
        # Label(FrameQHautPost, textvariable=self.QHautPost, bg="white", justify="left").pack()
        # self.QGauchePost.set(" Q Gauche : ")
        # Label(FrameQGauchePost, textvariable=self.QGauchePost, bg="white", justify="left").pack()
        # self.QDroitePost.set(" Q Droite : ")
        # Label(FrameQDroitePost, textvariable=self.QDroitePost, bg="white", justify="left").pack()
        # self.QBasPost.set(" Q Bas : ")
        # Label(FrameQBasPost, textvariable=self.QBasPost, bg="white", justify="left").pack()
    
    def onselect(self,evt):
        w = evt.widget
        if (len(w.curselection()) > 0):
            index = int(w.curselection()[0])
            value = w.get(index)
            # self.replaySimulationQuestion(value)

    def resetAction(self) :
        self.agent.epsilon = 1.0

    def chargerPoidsAction(self):
        if (os.path.exists("Weights_Model.wm.index")):
            self.agent.load("Weights_Model.wm")
            showinfo('OK', 'Succesfully loaded !')
        else:
            showinfo('Not OK', 'Failed at loading !')

    # def stringfromAccumulateurActions(self):
    #     s = "Sim " + str(self.replayLearningList.size()) + " : "
    #     # print("accumulateur d'actions ", self.framePrincipale.FrameEcranControle.AccumulateurActions)
    #     for i in self.framePrincipale.FrameEcranControle.AccumulateurActions:
    #         s += (int2Action2String1Char(i))
    #     return s

    def simuPostLearning(self,agent):
        state_size = self.envPost.state_size
        action_size = self.envPost.action_size
        state = self.envPost.reset()
        state = state * (1 / float(self.envPost.state.grid_size))
        state = np.reshape(state, [1, state_size])
        score_cumul = 0
        for time in range(200):
            act_values = agent.model.predict(state)
            action = np.argmax(act_values[0])
            next_state, reward, done = self.envPost.step(action)
            score_cumul += reward
            state = next_state * (1 / self.envPost.state.grid_size)
            state = np.reshape(state, [1, 4])
            if done :
                break
        return score_cumul

    def distance(self,state):
        goal = [self.env.state.goalx, self.env.state.goaly]
        d = abs(state[0]-goal[0]) + abs(state[1]-goal[1])
        return d

    def launchHRLAction(self) : 
        state_size = self.env.state_size
        self.framePrincipale.FrameEcranControle.ResetAction()
        self.envPost = GoToTheGoalEnv2D()

        done = False
        batch_size = 1
        Episodes = 100
        scores_app = []
        scores_evo = []

        for e in range(Episodes):
            score_cumul = 0
            state = self.env.reset()
            state = state * (1 / float(self.env.state.grid_size))
            state = np.reshape(state, [1, state_size])
            self.framePrincipale.FrameEcranControle.AccumulateurActions = []
            # print("Epoque : " , e)
            
            for time in range(200):

                # print("        state : " , state, end = "  ")

                # agent execute l'action en fonction de l'état reçu en argument
                action = self.agent.act(state)
                predictions = self.agent.model.predict(state)

                # print("        action : " , action, end = "  ")

                # updateStep realise un step en actualisant la vue et demande au user son avis sur l'action
                next_state, reward, done = self.updateStep(action)

                # print("        reward : " , reward)
                

                next_state = next_state * (1 / float(self.env.state.grid_size))
                next_state = np.reshape(next_state, [1, state_size])

                self.agent.remember(state, action, reward, next_state, done)

                self.framePrincipale.FrameEcranControle.AccumulateurActions.append(action)    

                score_cumul += reward

               
                
                if done:
                    #self.replayLearningList.insert(END,self.stringfromAccumulateurActions())
                    print("episode: {}/{}, score: {}, e: {:.5}"
                           .format(e + 1, Episodes, score_cumul, self.agent.epsilon))
                    break
                    
                # self.var.set(0)
                # self.HumanActionButton1.wait_variable(self.var)

                
                
                # Apprentissage 
                if len(self.agent.memory) > batch_size:
                    self.agent.replay(batch_size)

                    if (e%20) :
                        # Ajouter modif Qtable 
                        self.framePrincipale.FrameQMap.update_Qmap()
                        # self.agent.memory.clear()

            # Q-values for old state before human reward
            # self.QGaucheAnt.set(" Q Gauche : " + str(predictions[0][0])[:5])
            # self.QDroiteAnt.set(" Q Droite : " + str(predictions[0][1])[:5])
            # self.QHautAnt.set(" Q Haut : " + str(predictions[0][2])[:5])
            # self.QBasAnt.set(" Q Bas : " + str(predictions[0][3])[:5])

            # # Q-values for old state after human reward
            # self.QGauchePost.set(" Q Gauche : " + str(self.agent.model.predict(old_state)[0][0])[:5])
            # self.QDroitePost.set(" Q Droite : " + str(self.agent.model.predict(old_state)[0][1])[:5])
            # self.QHautPost.set(" Q Haut : " + str(self.agent.model.predict(old_state)[0][2])[:5])
            # self.QBasPost.set(" Q Bas : " + str(self.agent.model.predict(old_state)[0][3])[:5])

            # print("predictions avant : ",predictions)
            # print("predictions après : ",self.agent.model.predict(old_state))


            # si juge ! 
            # tm.sleep(3.0)

            scores_app.append(score_cumul)
            scores_evo.append(self.simuPostLearning(self.agent))


            #if(e % 15 == 0):
                #self.calculatePredictionMapAction()
                #self.update()

        try:
            self.agent.save("Weights_Model.wm")
        except:
            showinfo('Not OK', 'Failed at saving weight !')

        plt.plot(scores_app, 'g+')
        # plt.plot(scores_evo, 'b+')  
          
        plt.show() 


    # def switchReward(self, i):
    #     switcher={
    #         0: 0,
    #         1: 2 / 200,
    #         2: -10 / 200
    #     }
    #     return switcher.get(i,"Invalid reward")

    def switchReward(self, i):
        switcher={
            0: 0,
            1: 1/10, #4 / 239,
            2: -1/10, #-4 / 239
            3: 2/10,
            4: -2/10
        }
        return switcher.get(i,"Invalid reward")
        
    def juge(self, old_state, state):
        
        # self.var.set(0)
        # self.HumanActionButton1.wait_variable(self.var)

        # print("distance old: ", self.distance(old_state), end = "  ")
        # print("distance new : ", self.distance(state), end = "  ")
        if (self.distance(state) < self.distance(old_state)) :
            reward_human =  10 / 200
        else :
            reward_human = -10 / 200
        return reward_human

    def human_juge(self):
        reward_human = 0
        if self.var.get() == 1 :
            reward_human  = 20/200
        elif self.var.get() == 2 :
            reward_human = -20/200
        elif self.var.get() == 3 :
            reward_human = 0
        return reward_human


    def updateStep(self, numeroAction) : 
        old_state = [self.env.state.x, self.env.state.y]

        # On fait un pas de simulation
        next_state, reward, done = self.env.step(numeroAction)
        state = next_state[0:2]

        # Mise a jour des donnees de la frame de visualisation des etats
        # EtatAvant = self.framePrincipale.FrameVisualisation.FrameVisualisationState.EtatAvant
        # EtatApres = self.framePrincipale.FrameVisualisation.FrameVisualisationState.EtatApres
        # ActionRealisee = self.framePrincipale.FrameVisualisation.FrameVisualisationState.ActionRealisee

        # EtatAvant.set(EtatApres.get())
        # EtatApres.set("Position du mobile de déplacement : (" + str(self.env.state.x + 1) + ", " + str(self.env.state.y + 1) + ")")
        # ActionRealisee.set(int2Action2String(numeroAction))

        # On met a jour l'affichage graphique
        # self.framePrincipale.FrameVisualisation.UpdateCanvas(numeroAction)
        self.framePrincipale.FrameEcranControle.Update()

        # On ajoute cette action a la liste des actions realisees sur cette simulation
        self.framePrincipale.FrameEcranControle.AccumulateurActions.append(numeroAction)

        # Si la simulation est finie, on enregistre celle ci dans la liste des simus et on reset le simulateur
        if (done and not self.framePrincipale.FrameEcranControle.inSimulation):
            # self.framePrincipale.FrameEcranControle.AddSimuInList()
            self.framePrincipale.FrameEcranControle.ResetAction()

        # demande à l'utilisateur de juger l'action
        # rewardHRL = int(input("Juger l'action : 1 : bien, 3 : genial, 0 : je ne sais pas, 2 : nul, 4 : vraiment nul  "))
        # rewardHRLNorm = self.switchReward(rewardHRL)



        # JUGE AUTO
        reward_human = self.juge(old_state, state) 

        # JUGE HUMAIN
        # reward_human = self.human_juge()

        reward = reward + reward_human
        
        # Recompense = self.framePrincipale.FrameVisualisation.FrameVisualisationState.Recompense
        # Recompense.set(str(reward))
        self.framePrincipale.FrameEcranControle.AjouteScore(reward)
        self.framePrincipale.FrameEcranControle.Update()

        
        
        return next_state, reward, done
