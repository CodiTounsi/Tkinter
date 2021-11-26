#X_O by CodiTounsi
import tkinter as tk

player1Color = "#ca3537"
player2Color = "#152d51"
textColorPlayer1 = "#152d51"
textColorPlayer2 = "#ca3537"
labelColor = "orange"
labelTextColor = "blue"
btnResetColor = "black"
btnResetTextColor = "grey"

def reset():
    for i in range(3):
        for j in range(3):
            board[i][j].configure(
                text='', bg="SystemButtonFace"
                )


def isWin():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] \
                == board[i][2]['text'] != '':
            return 1
    for j in range(3):
        if board[0][j]['text'] == board[1][j]['text'] \
                == board[2][j]['text'] != '':
            return 1
    if board[0][0]['text'] == board[1][1]['text'] \
            == board[2][2]['text'] != '':
        return 1
    elif board[0][2]['text'] == board[1][1]['text'] \
            == board[2][0]['text'] != '':
        return 1
    elif EmptyCells() == []:
        return 0
    else:
        return -1

def EmptyCells():
    h=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == '':
                h.append((i,j))
    return h


player = 'O'
def main_gameflow(r,c):
    global player
    if board[r][c]['text'] == '' and isWin() == -1:
        if player == 'O':
            board[r][c].configure(
                text='O',bg = player1Color,
                fg= textColorPlayer1
                )
            if isWin() == -1:
                player = 'X'
                winAndTurnLabel.configure(text=("It's X's turn"))
            elif isWin() == 1:
                winAndTurnLabel.configure(text=("O win"))
            elif isWin() == 0:
                winAndTurnLabel.configure(text="Draw!")
        elif player == == 0:
winAndTurnL 'X':
            board[r][c].configure(
                text='X',bg = player2Color,
                fg= textColorPlayer2
                )
            if isWin() == -1:
                player = 'O'
                winAndTurnLabel.configure(text=("It's O's turn"))
           text='',fon elif isWin() == 1:
                winAndTurnLabel.configure(text=("X win"))
            elif isWin() == 0:
                winAndTurnLabel.configure(text="Draw!")


screen=tk.Tk()
screen.title('X O By CodiTounsi')
board=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        board[i][j]=tk.Button(
            text='',font=('normal',60,'normal'),width=4,height=1,
            command=lambda row = i,col = j: main_gameflow(row,col)
            )
        board[i][j].grid(row=i,column=j)


winAndTurnLabel=tk.Label(text="It's O's turn",font=('normal',22,'bold'),
                         bg = labelColor,fg = labelTextColor)
winAndTurnLabel.grid(row=3,column=1)
ResetButton=tk.Button(
    text='RESET',font=('Courier',18,'bold'),
    fg=btnResetTextColor,bg = btnResetColor,command=reset)
ResetButton.grid(row=4,column=1)

screen.mainloop()
