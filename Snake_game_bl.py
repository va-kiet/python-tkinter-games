from tkinter import *
import random

SPACE_SIZE = 18 #size of a block (in pixel)
GAME_WIDTH = 31
GAME_HEIGHT = 21
WIDTH = SPACE_SIZE*GAME_WIDTH   #height and width of the game
HEIGHT = SPACE_SIZE*GAME_HEIGHT 
SPEED = 150
BODY = 4
SNAKE_COLOR = '#41e82a'
FOOD_COLOR = 'red'
BG_COLOR = 'black'
score = 0
direction = 'down'

def new_game():
    class Snake():
        def __init__(self):
            self.body_size = BODY
            self.coordinates = []
            self.squares = []
            for i in range(0,BODY):
                self.coordinates.append([((WIDTH/SPACE_SIZE-1)/2)*SPACE_SIZE,((HEIGHT/SPACE_SIZE-1)/2)*SPACE_SIZE])

            for x,y in self.coordinates:
                square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag='snake')
                self.squares.append(square)
    class Smells_Like_Food():
        def __init__(self):
            x = random.randint(0,(WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
            y = random.randint(0,(HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
            for i,j in block.block_coord:
                while x == i and y == j:
                    x = random.randint(0,(WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
                    y = random.randint(0,(HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
            for i,j in snake.coordinates:
                while x == i and y == j:
                    x = random.randint(0,(WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
                    y = random.randint(0,(HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

            self.coordinates = [x,y]
            canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag='food')

    class Something_in_the_way():
        def __init__(self):
            global direction
            mode = random.randint(0,6)
            self.block_coord = []
            if mode == 0:
                x = int(round((WIDTH/SPACE_SIZE)/5))*SPACE_SIZE
                y = int(round((HEIGHT/SPACE_SIZE)/5))*SPACE_SIZE
                for xy in range(y,HEIGHT-y,SPACE_SIZE):
                    self.block_coord.append([x,xy])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,xy])
                
            elif mode == 1:
                x = int(round((WIDTH/SPACE_SIZE)/5))*SPACE_SIZE
                y = 0
                for xy in range(y,int(HEIGHT/5)*2,SPACE_SIZE):
                    self.block_coord.append([x,xy])
                    self.block_coord.append([x,HEIGHT-xy-SPACE_SIZE])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,xy])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,HEIGHT-xy-SPACE_SIZE])

            elif mode == 2:
                x = int(round((WIDTH/SPACE_SIZE)/5))*SPACE_SIZE
                y = int(round((HEIGHT/SPACE_SIZE)/5))*SPACE_SIZE
                for xy in range(y,y+y,SPACE_SIZE):
                    self.block_coord.append([x,xy])
                    self.block_coord.append([x,HEIGHT-xy-SPACE_SIZE])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,xy])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,HEIGHT-xy-SPACE_SIZE])
                for xx in range(x,x+x,SPACE_SIZE):
                    self.block_coord.append([xx,y])
                    self.block_coord.append([WIDTH-xx-SPACE_SIZE,y])
                    self.block_coord.append([xx,HEIGHT-y-SPACE_SIZE])
                    self.block_coord.append([WIDTH-xx-SPACE_SIZE,HEIGHT-y-SPACE_SIZE])

            elif mode == 3:
                x = int(round((WIDTH/SPACE_SIZE)/5))*SPACE_SIZE*2
                y = int(round((HEIGHT/SPACE_SIZE)/5))*SPACE_SIZE*4
                for xx in range(0,x+SPACE_SIZE,SPACE_SIZE):
                    self.block_coord.append([xx,y])
                    self.block_coord.append([WIDTH-xx-SPACE_SIZE,HEIGHT-y-SPACE_SIZE])
                for xy in range(0,y,SPACE_SIZE):
                    self.block_coord.append([x,xy])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,HEIGHT-xy-SPACE_SIZE])

            elif mode == 4:
                direction = 'right'
                x = int(round((WIDTH/SPACE_SIZE)/5))*SPACE_SIZE
                y = int(round((HEIGHT/SPACE_SIZE)/5))*SPACE_SIZE*2
                z = int(round((HEIGHT/SPACE_SIZE)/5))*SPACE_SIZE*3
                for xx in range(0,x+SPACE_SIZE,SPACE_SIZE):
                    self.block_coord.append([xx,y])
                    self.block_coord.append([WIDTH-xx-SPACE_SIZE,HEIGHT-y-SPACE_SIZE])
                for xz in range(z,WIDTH,SPACE_SIZE):
                    self.block_coord.append([xz,y])
                    self.block_coord.append([WIDTH-xz-SPACE_SIZE,HEIGHT-y-SPACE_SIZE])
                for xy in range(0,y,SPACE_SIZE):
                    self.block_coord.append([x,xy])
                    self.block_coord.append([WIDTH-x-SPACE_SIZE,HEIGHT-xy-SPACE_SIZE])
                    self.block_coord.append([z,xy])
                    self.block_coord.append([WIDTH-z-SPACE_SIZE,HEIGHT-xy-SPACE_SIZE])

            elif mode == 5:
                pass

            elif mode == 6:
                direction = 'right'
                for x in range(0,WIDTH,SPACE_SIZE):
                    self.block_coord.append([x,0])
                    self.block_coord.append([x,HEIGHT-SPACE_SIZE])
                for y in range(0,HEIGHT,SPACE_SIZE):
                    self.block_coord.append([0,y])
                    self.block_coord.append([WIDTH-SPACE_SIZE,y])

            for x,y in self.block_coord:
                canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill='silver',tag='block')

    def next_turn(snake,food):
        x,y = snake.coordinates[0]
        if direction == 'up':
            y-= SPACE_SIZE
            if y < 0:
                y=HEIGHT-SPACE_SIZE
        elif direction == 'down':
            y+= SPACE_SIZE
            if y >= HEIGHT:
                y=0
        elif direction == 'right':
            x+= SPACE_SIZE
            if x >= WIDTH:
                x=0
        elif direction == 'left':
            x-= SPACE_SIZE
            if x < 0:
                x=WIDTH-SPACE_SIZE
    
        snake.coordinates.insert(0,(x,y))
        square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
        snake.squares.insert(0,square)
        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score 
            score += 1
            label.config(text='Score: {}'.format(score))
            canvas.delete('food')
            food = Smells_Like_Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
        if check_colissions(snake):
            game_over()
        else:
            interface.after(SPEED,next_turn,snake,food)

    def key_control(key_presseds):
        global direction,SPEED
        if key_presseds == 'left':
            if direction != 'right':
                direction = key_presseds
        elif key_presseds == 'right':
            if direction != 'left':
                direction = key_presseds
        elif key_presseds == 'up':
            if direction != 'down':
                direction = key_presseds
        elif key_presseds == 'down':
            if direction != 'up':
                direction = key_presseds
        elif key_presseds == 'new game':
            play_again()
        elif key_presseds == '-':
            SPEED += 50
        elif key_presseds == '+':
            if SPEED >= 100:
                SPEED -= 50
            else:
                pass
    def check_colissions(snake):
        x,y = snake.coordinates[0]
        for body in snake.coordinates[1:]:
            if x == body[0] and y == body[1]:
                return True
        for i,j in block.block_coord:
            if x == i and y == j:
                return True

        return False
    def game_over():

        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text='GAME OVER',font=('consolas',30,'bold'),fill='blue',tag='gameover')
        Button(interface,text='Play Again',font=('consolas',20),command=play_again,fg='red',bg='#41e82a').place(x=canvas.winfo_width()/2-85,y=canvas.winfo_height()/2+70)

    def play_again():
        global score,direction
        interface.destroy()
        score = 0
        direction = 'down'
        new_game()


    interface = Tk()
    interface.title('Snake Game')
    interface.resizable(False,False)
    logo = PhotoImage(file='Snake.png')
    interface.iconphoto(True,logo)

    
    label = Label(interface,text='Score: {}'.format(score),font=('arial',20))
    label.pack()
    canvas = Canvas(interface,bg=BG_COLOR,width=WIDTH,height=HEIGHT)
    canvas.pack()
    interface.update()

    screen_width = interface.winfo_screenwidth()
    screen_height = interface.winfo_screenheight()
    interface_width = interface.winfo_width()
    interface_height = interface.winfo_height()
    x = int(screen_width/2 - interface_width/2)
    y = int(screen_height/2 - interface_height/2)
    interface.geometry("{}x{}+{}+{}".format(interface_width,interface_height,x,y))
    interface.bind('<Left>',lambda event: key_control('left'))
    interface.bind('<Right>',lambda event: key_control('right'))
    interface.bind('<Up>',lambda event: key_control('up'))
    interface.bind('<Down>',lambda event: key_control('down'))
    interface.bind('<q>',lambda event: key_control('new game'))
    interface.bind('<minus>',lambda event: key_control('-'))
    interface.bind('<equal>',lambda event: key_control('+'))
    interface.bind('<plus>',lambda event: key_control('+'))
    block = Something_in_the_way()
    snake = Snake()
    food = Smells_Like_Food()
    next_turn(snake,food)
    interface.mainloop()

if __name__ == '__main__':
    new_game()
