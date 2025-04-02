import tkinter as tk
from tkinter import messagebox
from State import State
from Action import Action
from Optimal import Optimal
from QLearning import Q_Learning
from Nim import Nim 

class NimGameUI:
    def __init__(self, root, state):
        self.root = root
        self.root.title("Global Nim Game")

        self.state = state
        self.optimal = Optimal()

        self.qAgent = Q_Learning(0.9865207839026998,0.3469818790482299,1,0,0.9084777590998696,484)
        opponent = Q_Learning(0.9533018424132107,0.08611300361820182,1,0,0.9004614408879907,438)
        training = Nim(self.qAgent,opponent,200000)
        training.play(self.state,True)



        self.gridrow = 10
        self.gridcolumn = 10
        self.frame = tk.Frame(root, width=400, height=400, bg="black")
        self.frame.grid(row=1, column=0)
        self.frame.grid_propagate(False)
        self.controlpanel = tk.Frame(root,width=400,height = 100)
        self.controlpanel.grid(row = 2, column = 0)

        self.create_buttons()
    
    def create_buttons(self):
        self.status_label = tk.Label(self.controlpanel, text='Max removal: ' + str(self.state.max_removal))
        self.status_label.grid(row = 0, column = 0)
        
        if self.state.num_acts %2 == 0:
          text = 'Player 1'
        else:
          text = 'Player 2'
        playerLabel = tk.Label(self.controlpanel, text = 'Turn: '+text)
        playerLabel.grid(row = 1, column = 0)

        
        Optimalbutton = tk.Button(self.controlpanel, text = 'Play against Optimal Agent', command = self.optButton )
        Optimalbutton.grid(row = 2, column = 0)
        Qbutton = tk.Button(self.controlpanel, text = 'Play against Q Learning Agent', command = self.qButton)
        Qbutton.grid(row = 3 , column = 0)

        state = self.state.state
        for i in range(len(state)):
            for j in range(state[i]):
                button  = tk.Button(self.frame, text= '', command=lambda i=i, j=j: self.act(i,state[i]-j))
                button.grid(row = self.gridrow - j, column = i +1)

    def act(self, pile,removal):
        action = Action((pile,removal))

        if self.state.isValid(action):
          self.state.doAction(action)
          for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Button):
              widget.destroy()
          state = self.state.state
          for i in range(len(state)):
            for j in range(state[i]):
                button  = tk.Button(self.frame, text='', command=lambda i=i, j=j: self.act(i,state[i]-j))
                button.grid(row = self.gridrow - j, column = i +1)
          print(self.state)
          self.create_buttons()

        else:
          print('Not a valid move, try again')
        return action
    
    def optButton(self):
       move = self.optimal.optPolicy(self.state)
       if move is not None:
         self.act(move.action[0],move.action[1])


    def qButton(self):
       if self.state.isTerminal():
          return
       move = self.qAgent.updateQ(self.state)
       if move is not None:
          self.act(move.action[0],move.action[1])



root = tk.Tk()
game = NimGameUI(root, State([1,2,3,4,5],4))
root.mainloop()

