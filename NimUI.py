import tkinter as tk
from tkinter import messagebox
from State import State
from Action import Action

class NimGameUI:
    def __init__(self, root, state):
        self.root = root
        self.root.title("Global Nim Game")
        self.state = state
        self.gridrow = max(state.state)
        self.gridcolumn = len(state.state)
        self.frame = tk.Frame(root, width=400, height=400, bg="black")
        self.frame.grid(row=self.gridrow, column=self.gridcolumn)
        self.frame.grid_propagate(False)
        self.create_buttons()
    
    def create_buttons(self):
        self.status_label = tk.Label(self.frame, text='Max removal: ' + str(self.state.max_removal))
        self.status_label.grid(row = 0, column = 0)
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
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
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



root = tk.Tk()
game = NimGameUI(root, State([1,2,3,4,5,6,7,8],4))
root.mainloop()

