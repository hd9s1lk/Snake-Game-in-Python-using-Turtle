import turtle, winsound
import time
import random

delay = 0.1
score = 0
high_score = 0

corpo = []

window = turtle.Screen()
window.title("Snake Game by Henrique!")
window.bgcolor("green")
window.setup(width=1920, height=1080)
window.tracer(0)


#character
boneco = turtle.Turtle()
boneco.speed(0)
boneco.shape("square")
boneco.color("white")
boneco.penup()
boneco.goto(0,0)
boneco.direction = "stop"


#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 450)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


def cima():
    if boneco.direction != "down":
        boneco.direction = "up"
def baixo():
    if boneco.direction != "up":
        boneco.direction = "down"
def direita():
    if boneco.direction != "left":
        boneco.direction = "right"
def esquerda():
    if boneco.direction != "right":
        boneco.direction = "left"



#movimento

def mover():
    if boneco.direction == "up":
        y = boneco.ycor()
        y += 20
        boneco.sety(y)


    if boneco.direction == "down":
        y = boneco.ycor()
        y -= 20
        boneco.sety(y)

    if boneco.direction == "right":
        x = boneco.xcor()
        x += 20
        boneco.setx(x)

    if boneco.direction == "left":
        x = boneco.xcor()
        x -= 20
        boneco.setx(x)




#key bindings

window.listen()
window.onkeypress(cima, "w")
window.onkeypress(baixo, "s")
window.onkeypress(esquerda, "a")
window.onkeypress(direita, "d")



while True:
    window.update()


    #colisão com borders

    if boneco.xcor() > 350 or boneco.xcor() < -350 or boneco.ycor() > 500 or boneco.ycor() < -500:
        time.sleep(0.5)
        boneco.goto(0,0)
        boneco.direction = "stop"
        winsound.PlaySound("Fortnite Death Sound Effect.wav", winsound.SND_ASYNC)
    
        for add_corpo in corpo:
            add_corpo.goto(2000,2000)

        corpo.clear()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))




    if boneco.distance(food) < 20:
        x = random.randint(-350,350)
        y = random.randint(-500,500)
        food.goto(x,y)
        winsound.PlaySound("Minecraft Eating.wav", winsound.SND_ASYNC)

        add_corpo = turtle.Turtle()
        add_corpo.speed(0)
        add_corpo.shape("square")
        add_corpo.color("black")
        add_corpo.penup()
        corpo.append(add_corpo)

        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        delay -= 0.001

    for i in range(len(corpo) -1, 0 , -1):
        x = corpo[i-1].xcor()
        y = corpo[i-1].ycor()
        corpo[i].goto(x,y)

    if len(corpo) > 0:
        x = boneco.xcor()
        y = boneco.ycor()
        corpo[0].goto(x,y)




    mover()

    #colisão com o corpo
    for add_corpo in corpo:
        if add_corpo.distance(boneco) < 20:
            time.sleep(1)
            boneco.goto(0,0)
            boneco.direction = "stop"
            winsound.PlaySound("Minecraft Eating.wav", winsound.SND_ASYNC)

            for add_corpo in corpo:
                add_corpo.goto(2000,2000)

            corpo.clear()
            

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

window.mainloop()