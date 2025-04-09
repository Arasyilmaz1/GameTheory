import tkinter as tk
from tkinter import messagebox
from State import State
from Action import Action
from Optimal import Optimal
from QLearning import Q_Learning
from Nim import Nim 

class NimGameUI:
    def __init__(self, root, state):
        self.initState = State(state.state,state.max_removal)
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

        self.starting_screen()

    def starting_screen(self):
       game_name = tk.Label(self.frame, text = 'Global Fibonacci \n Nim',font=("Braggadocio", 30), fg = 'white',bg = 'black')
       game_name.place(relx=0.5, rely=0.5, anchor="center")
       playButton = tk.Button(self.controlpanel ,text = 'Play',bg ='blue', font = ("Braggadocio",26), command = self.play, )
       playButton.place(relx=0.5, rely=0.5, anchor="center")

    def play(self):
       self.reset_screen()
       self.create_buttons()
    
    def create_buttons(self):
        if self.state.isTerminal():
           self.reset_screen()
           self.finish_screen()
           return
        self.status_label = tk.Label(self.controlpanel, text='Max removal: ' + str(self.state.max_removal))
        self.status_label.grid(row = 0, column = 0)
        
        if self.state.num_acts %2 == 0:
          text = 'Player 1'
        else:
          text = 'Player 2'
        playerLabel = tk.Label(self.controlpanel, text = 'Turn: '+text)
        playerLabel.grid(row = 1, column = 0)

        
        Optimalbutton = tk.Button(self.controlpanel, text = 'Play against Optimal Agent move', command = self.optButton )
        Optimalbutton.grid(row = 2, column = 0)
        Qbutton = tk.Button(self.controlpanel, text = 'Q Learning Agent move', command = self.qButton)
        Qbutton.grid(row = 3 , column = 0)

        state = self.state.state
        for i in range(len(state)):
            for j in range(state[i]):
                button  = tk.Button(self.frame, text= '', borderwidth=1,command=lambda i=i, j=j: self.act(i,state[i]-j))
                button.grid(row = self.gridrow - j, column = i +1 )

    def act(self, pile,removal):   
        action = Action((pile,removal))
        if self.state.isValid(action):
          self.state.doAction(action)
          for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Button):
              widget.grid_forget()
          state = self.state.state
          for i in range(len(state)):
            for j in range(state[i]):
                button  = tk.Button(self.frame, text='',borderwidth=1, command=lambda i=i, j=j: self.act(i,state[i]-j))
                button.grid(row = self.gridrow - j, column = i +1)
          print(self.state)
          self.create_buttons()

        else:
          print('Not a valid move, try again')
        return action
    
    def optButton(self):
       if self.state.isTerminal():
          return
       move = self.optimal.optPolicy(self.state)
       if move is not None:
         self.act(move.action[0],move.action[1])


    def qButton(self):
       if self.state.isTerminal():
          return
       move = self.qAgent.updateQ(self.state)
       if move is not None:
          self.act(move.action[0],move.action[1])

    def reset_screen(self):
       for widget in self.frame.winfo_children():
            widget.destroy()
       for widget in self.controlpanel.winfo_children():
            widget.destroy()

    def finish_screen(self):
       winner = tk.Label(self.frame,text = '', fg = 'white',font = ("Braggadocio", 20))
       winner.place(relx=0.5,rely=0.5,anchor='center')
       restartButton = tk.Button(self.controlpanel,text='Restart', fg='black',font = ("Braggadocio", 26),command = self.restart)
       restartButton.place(relx=0.5,rely=0.5,anchor='center')
       if self.state.num_acts %2 == 0:
            winner.config(text = 'Player 2 wins!! \n Congratulations Player 2!' )
       else:
            winner.config(text = 'Player 1 wins!!\n Congratulations Player 1!')

    def restart(self):
       self.reset_screen()
       self.state = State(self.initState.state,self.initState.max_removal)
       self.starting_screen()
       



root = tk.Tk()
game = NimGameUI(root, State([1,2,3,4,5],4))
root.mainloop()

