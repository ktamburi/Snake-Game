import turtle
import tkinter as TK
import time
import random

#window setup
wn=turtle.Screen() 
wn.setup(width=700,height=650) 
root = wn.getcanvas().winfo_toplevel() 
root.resizable(False, False) 
wn.title("Snake Game by Bob Ndertusat") 
wn.bgcolor('#60D164') 
wn.tracer(0) 

#Pen and scores
score=0 
high_score=0 
pen=turtle.Turtle() 
pen.shape=("square") 
pen.penup() 
pen.hideturtle() 
pen.goto(0,305) 
pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier",12,"normal")) 

#function to speed up the snake
n=0.14
def speed():
    global n
    global score
    if ((score%5)==0 and n>0.05):
        n-=0.01

#def function to update score
def update_score():
    global score 
    global high_score
    score+=1
    if score>high_score:
        high_score=score
    pen.clear() 
    pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier",12,"normal")) 
    speed()

#snake head setup
head=turtle.Turtle() 
head.speed(0)   
head.color('#030721')  
head.shape("circle") 
head.shapesize(1.1) 
head.penup()    
head.goto(0,0)  
head.direction="stop" 

#snake initial body setup
body = [] 
for index in range(1,4,+1): 
    body_part=turtle.Turtle() 
    body_part.speed(0) 
    body_part.shape("circle") 
    body_part.color('#383fff') 
    body_part.penup() 
    body_part.goto(head.xcor()-(20*index),0) 
    body.append(body_part) 
    
#snake food
apple=turtle.Turtle()
apple.speed(0)  
apple.color("red") 
apple.shape("triangle")
apple.shapesize(0.8) 
apple.penup()    
apple.goto(80,0)  

#function to grow snake each time it feeds
def newbody():
    new_body_part=turtle.Turtle()
    new_body_part.speed(0)
    new_body_part.shape("circle")
    new_body_part.color('#383fff')
    new_body_part.penup()
    body.append(new_body_part) 
    
#function to update the movement of body
def bodymove():
    if head.direction=="left" or head.direction=="right" or head.direction=="up" or head.direction=="down":
        for index in range(len(body)-1,-1,-1):
            x=body[index-1].xcor()
            y=body[index-1].ycor()
            body[index].goto(x,y)        
            if index==0:
                x=head.xcor()
                y=head.ycor()
                body[0].goto(x,y)

#functions to update the movement of the snake
game=True 
def go_up():
    global game
    if head.direction !="down" and game!=False:
        head.direction="up"
def go_down():
    global game
    if head.direction !="up" and game!=False:
        head.direction="down"
def go_right():
    global game
    if head.direction !="left" and game!=False:
        head.direction="right"
def go_left():
    global game
    if head.direction !="right" and game!=False:
        head.direction="left"

#function determining how the snake head moves
def move(): 
    if head.direction=="up": 
        head.sety(head.ycor()+20) 
    if head.direction=="down": 
        head.sety(head.ycor()-20) 
    if head.direction=="left": 
        head.setx(head.xcor()-20) 
    if head.direction=="right": 
        head.setx(head.xcor()+20) 
        
#defining function for border collision
def border_collision():
    if head.xcor()>330 or head.xcor()<-330 or head.ycor()>305 or head.ycor()<-305:
        global game
        game=False
        head.direction="stop" 
        pen.penup() 
        pen.goto(0,0)
        pen.write("GAME OVER! Press 'R' to restart.", align="center", font=("Courier",12,"normal"))
        
#defining function for food collision
def food_collision():
    if head.distance(apple)<18:
        x=random.randint(-335,335)
        y=random.randint(-310,310)  
        apple.goto(x,y)
        newbody()
        update_score()   
        
#define function for body collision
def body_collision():
    for segment in body: 
        if head.distance(segment)<20:
            global game
            game=False
            head.direction="stop" 
            pen.penup() 
            pen.goto(0,0)
            pen.write("GAME OVER! Press 'R' to restart.", align="center", font=("Courier",12,"normal")) 

#pause and resume function       
temp="stop"
def pause():
    global temp
    global game
    if (head.direction != "stop"):
        temp=head.direction
        head.direction="stop"
        game=False
    else:
        head.direction=temp
        game=True
        temp="stop"

#defining function to set the snake to its initial conditions after game over
def restart(): 
    global game
    game=True
    global score
    score=0 
    global n
    n=0.14
    global temp
    temp="stop"
    for index in range(len(body)-1,-1,-1):
        body[index].hideturtle() 
    body.clear() 
    head.direction="stop"
    head.goto(0,0) 
    for index in range(1,4,+1):
        body_part=turtle.Turtle()
        body_part.speed(0)
        body_part.shape("circle")
        body_part.color('#383fff')
        body_part.penup()
        body_part.goto(0-(20*index),0)
        body.append(body_part)  
    apple.goto(80,0) 
    pen.clear() 
    pen.goto(0,305)
    pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier",12,"normal"))

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"W")
wn.onkeypress(go_up,"w")
wn.onkeypress(go_up,"Up") 
wn.onkeypress(go_down,"s") 
wn.onkeypress(go_down,"S") 
wn.onkeypress(go_down,"Down") 
wn.onkeypress(go_left,"a")
wn.onkeypress(go_left,"A")
wn.onkeypress(go_left,"Left") 
wn.onkeypress(go_right,"D")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_right,"Right")
wn.onkeypress(restart,"R")
wn.onkeypress(restart,"r")
wn.onkeypress(pause,"P")
wn.onkeypress(pause,"p")

while True:
    wn.update()
    border_collision()
    food_collision()
    bodymove()
    move()
    body_collision()
    time.sleep(n)