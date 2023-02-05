from tkinter import *
import Tic_Tac_Toe_mode

players = ['x','o']
player = players[0]
def launch():
    def new_game():
        global player
        player = players[0]
        for row in range(3):
            for column in range(3): 
                button[row][column].config(text='',bg='#F0F0F0')
        label.config(text=player+' turn',fg='red')

    def next_turn(row,column):
        global player
        if button[row][column]['text'] == '' and check_winner() is False:
            if player == players[0]:
                button[row][column].config(text=player,fg='red')
                if check_winner() is False:
                    player = players[1]
                    label.config(text=players[1]+' turn',fg='green')
                elif check_winner() is True:
                    label.config(text=players[0]+' win!')
                elif check_winner() == 'Tie':
                    label.config(text='Tie!')
            else:
                button[row][column].config(text=player,fg='green')
                if check_winner() is False:
                    player = players[0]
                    label.config(text=players[0]+' turn',fg='red')
                elif check_winner() is True:
                    label.config(text=players[1]+' win!')
                elif check_winner() == 'Tie':
                    label.config(text='Tie!')
        interface.update()
    def empty_space():
        spaces = 9
        for row in range(3):
            for column in range(3): 
                if button[row][column]['text'] != '':
                    spaces -= 1
        if spaces == 0:
            return False
        else:
            return True

    def check_winner():
        for row in range(3):
            if button[row][0]['text'] == button[row][1]['text'] == button[row][2]['text'] != '':
                if button[row][0]['text'] == players[0]:
                    for column in range(3):
                        button[row][column].config(bg='#ffaaa3')
                elif button[row][0]['text'] == players[1]:
                    for column in range(3):
                        button[row][column].config(bg='#c6ff44')
                return True
        for column in range(3):
            if button[0][column]['text'] == button[1][column]['text'] == button[2][column]['text'] != '':
                if button[0][column]['text'] == players[0]:
                    for row in range(3):
                        button[row][column].config(bg='#ffaaa3')
                elif button[0][column]['text'] == players[1]:
                    for row in range(3):
                        button[row][column].config(bg='#c6ff44')
                return True
        if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != '':
            if button[0][0]['text'] == players[0]:
                    for i in range(3):
                        button[i][i].config(bg='#ffaaa3')
            elif button[0][0]['text'] == players[1]:
                    for i in range(3):
                        button[i][i].config(bg='#c6ff44')
            return True
        if button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] != '':
            if button[0][2]['text'] == players[0]:
                    for i in range(3):
                        button[i][2-i].config(bg='#ffaaa3')
            elif button[0][2]['text'] == players[1]:
                    for i in range(3):
                        button[i][2-i].config(bg='#c6ff44')
            return True
        if empty_space() is False:
            for row in range(3):
                for column in range(3):
                    button[row][column].config(bg='yellow')
            return 'Tie'
        else:
            return False

    def quit():
        interface.destroy()
        Tic_Tac_Toe_mode.launch()

    interface = Tk()
    interface.title('Tic Tac Toe')
    interface.resizable(False,False)
    button = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    
    frame = Frame(interface)
    frame.pack()

    restart_button = Button(frame,text='Restart',font=('consolas',15),width=8,command=new_game)
    restart_button.pack(side=LEFT)

    quit_button = Button(frame,text='Quit',font=('consolas',15),width=8,command=quit)
    quit_button.pack(side=LEFT)

    label = Label(text=player+' turn',font=('consolas',25),fg='red')
    label.pack(side=TOP)

    frames = Frame(interface)
    frames.pack()

    for row in range(3):
        for column in range(3):
            button[row][column] = Button(frames,text='',font=('consolas',40),width=5,height=2,
                                         command=lambda row=row,column=column : next_turn(row,column))
            button[row][column].grid(row=row,column=column)
    interface.mainloop()

if __name__ == '__main__':
    launch()


