from tkinter import *
import Tic_Tac_Toe
import Caro
import Caro_br

def launch():
    def mode3():
        interface.destroy()
        Tic_Tac_Toe.launch()

    def mode5():
        interface.destroy()
        Caro.launch()

    def modebr():
        interface.destroy()
        Caro_br.launch()
    interface = Tk()
    interface.title('Mode Selection')
    interface.config(bg='#ffd966')
    interface.geometry('720x200')
    interface.resizable(False,False)
    Label(interface,text='Tic Tac Toe Mode Selection:',font=('Ink Free',20),bg='#ffd966',fg='#351c75').place(x=200,y=20)
    Button(interface,text='Tic Tac Toe\n(3x3)',font=('consolas',15),command=mode3,width=17,bg='#8fce00',fg='red').place(x=40,y=80)
    Button(interface,text='Caro\n(five in a row)',font=('consolas',15),command=mode5,width=17,bg='yellow',fg='red').place(x=260,y=80)
    Button(interface,text='Caro\n(block rules)',font=('consolas',15),command=modebr,width=17,bg='cyan',fg='red').place(x=480,y=80)

    interface.mainloop()
if __name__ == '__main__':
    launch()
