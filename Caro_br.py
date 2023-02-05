from tkinter import *
import Tic_Tac_Toe_mode

players = ['x','o']
player = players[0]
def launch():
    def new_game():
        global player
        player = players[0]
        for row in range(20):
            for column in range(30): 
                button[row][column].config(text='',bg='#F0F0F0')
        label.config(text=player+' turn',fg='red')

    def next_turn(row,column):
        global player
        if button[row][column]['text'] == '' and check_winner() != True:
            if player == players[0]:
                button[row][column].config(text=player,fg='red')
                if check_winner() != True:
                    player = players[1]
                    label.config(text=players[1]+' turn',fg='green')
                elif check_winner() is True:
                    label.config(text=players[0]+' win!')
            else:
                button[row][column].config(text=player,fg='green')
                if check_winner() != True:
                    player = players[0]
                    label.config(text=players[0]+' turn',fg='red')
                elif check_winner() is True:
                    label.config(text=players[1]+' win!')
        interface.update()

    def check_winner():
        for row in range(20):
            for column in range(26):
                if button[row][column]['text'] == button[row][column+1]['text'] == button[row][column+2]['text'] == button[row][column+3]['text'] == button[row][column+4]['text'] != '':
                    if column != 0 and column != 15:
                        if button[row][column]['text'] == players[0] and not (button[row][column-1]['text'] == button[row][column+5]['text'] == players[1]):
                            for i in range(5):
                                button[row][column+i].config(bg='#ffaaa3')
                            return True
                        elif button[row][column]['text'] == players[1] and not (button[row][column-1]['text'] == button[row][column+5]['text'] == players[0]):
                            for i in range(5):
                                button[row][column+i].config(bg='#c6ff44')
                            return True
                    else:
                        if button[row][column]['text'] == players[0]:
                            for i in range(5):
                                button[row][column+i].config(bg='#ffaaa3')
                        elif button[row][column]['text'] == players[1]:
                            for i in range(5):
                                button[row][column+i].config(bg='#c6ff44')
                        return True
        for column in range(30):
            for row in range(16):
                if button[row][column]['text'] == button[row+1][column]['text'] == button[row+2][column]['text'] == button[row+3][column]['text'] == button[row+4][column]['text'] != '':
                    if row != 0 and row != 15:    
                        if button[row][column]['text'] == players[0] and not (button[row-1][column]['text'] == button[row+5][column]['text'] == players[1]):
                            for i in range(5):
                                button[row+i][column].config(bg='#ffaaa3')
                            return True
                        elif button[row][column]['text'] == players[1] and not (button[row-1][column]['text'] == button[row+5][column]['text'] == players[0]):
                            for i in range(5):
                                button[row+i][column].config(bg='#c6ff44')
                            return True
                    else:
                        if button[row][column]['text'] == players[0]:
                            for i in range(5):
                                button[row+i][column].config(bg='#ffaaa3')
                        elif button[row][column]['text'] == players[1]:
                            for i in range(5):
                                button[row+i][column].config(bg='#c6ff44')
                        return True
        for row in range(16):
            for column in range(26):
                if button[row][column]['text'] == button[row+1][column+1]['text'] == button[row+2][column+2]['text'] == button[row+3][column+3]['text'] == button[row+4][column+4]['text'] != '':
                    if (row != 0 and column != 0) and (row != 15 and column != 15):
                        if button[row][column]['text'] == players[0] and not (button[row-1][column-1]['text'] == button[row+5][column+5]['text'] == players[1]):
                            for i in range(5):
                                button[row+i][column+i].config(bg='#ffaaa3')
                            return True
                        elif button[row][column]['text'] == players[1] and not (button[row-1][column-1]['text'] == button[row+5][column+5]['text'] == players[0]):
                            for i in range(5):
                                button[row+i][column+i].config(bg='#c6ff44')
                            return True
                    else:
                        if button[row][column]['text'] == players[0]:
                            for i in range(5):
                                button[row+i][column+i].config(bg='#ffaaa3')
                        elif button[row][column]['text'] == players[1]:
                            for i in range(5):
                                button[row+i][column+i].config(bg='#c6ff44')
                        return True
                elif button[19-row][column]['text'] == button[19-row-1][column+1]['text'] == button[19-row-2][column+2]['text'] == button[19-row-3][column+3]['text'] == button[19-row-4][column+4]['text'] != '':
                    if (row != 0 and column != 0) and (row != 15 and column != 15):
                        if button[19-row][column]['text'] == players[0] and not (button[19-row+1][column-1]['text'] == button[19-row-5][column+5]['text'] == players[1]):
                            for i in range(5):
                                button[19-row-i][column+i].config(bg='#ffaaa3')
                            return True
                        elif button[19-row][column]['text'] == players[1] and not (button[19-row+1][column-1]['text'] == button[19-row-5][column+5]['text'] == players[0]):
                            for i in range(5):
                                button[19-row-i][column+i].config(bg='#c6ff44')
                            return True
                    else:
                        if button[19-row][column]['text'] == players[0]:
                            for i in range(5):
                                button[19-row-i][column+i].config(bg='#ffaaa3')
                        elif button[19-row][column]['text'] == players[1]:
                            for i in range(5):
                                button[19-row-i][column+i].config(bg='#c6ff44')
                        return True
    def quit():
        interface.destroy()
        Tic_Tac_Toe_mode.launch()

    interface = Tk()
    interface.title('Caro (block rules)')
    interface.resizable(False,False)
    button = []
    for row in range(20):
        rows = []
        for column in range(30):
            rows = rows + [0]
        button = button + [rows]
    
    frame = Frame(interface)
    frame.pack()

    restart_button = Button(frame,text='Restart',font=('consolas',15),width=8,command=new_game)
    restart_button.pack(side=LEFT)

    quit_button = Button(frame,text='Quit',font=('consolas',15),width=8,command=quit)
    quit_button.pack(side=LEFT)

    label = Label(text=player+' turn',font=('consolas',17),fg='red')
    label.pack(side=TOP)

    frames = Frame(interface)
    frames.pack()

    for row in range(20):
        for column in range(30):
            button[row][column] = Button(frames,text='',font=('consolas',12),width=3,height=1,
                                         command=lambda row=row,column=column : next_turn(row,column))
            button[row][column].grid(row=row,column=column)
    interface.mainloop()

if __name__ == '__main__':
    launch()
