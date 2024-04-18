from turtle import Turtle, Screen
import time
import random

# Proměnné
score = 0
highest_score = 0


screen = Screen()
screen.bgcolor("green")
screen.title("Vítejte v Hadí hře")
screen.setup(width=600, height=600)
screen.tracer(False)



# Hadí hlava, jablko, skóre
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

apple = Turtle ("circle")
apple.color ("red")
apple.penup()
apple.goto (100, 100)

score_sign = Turtle ("square")
score_sign.speed (0)
score_sign.color ("white")
score_sign.penup ()
score_sign.hideturtle ()
score_sign.goto (0, 265)
score_sign.write (f"Skóre: 0   Nejvyšší skóre: 0", align="center", font=18)


body_parts = []


def move ():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx (x + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx (x - 20)

# Funkce
def move_up():
    if head.direction != "down":
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_left():
    if head.direction != "right":
        head.direction = "left"
def move_right():
    if head.direction != "left":
        head.direction = "right"

# Kliknutí na klávesy
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

   

# Hlavní cyklus
while True:
    screen.update()
    
    # Kontrola kolize s hranou 
    if head.xcor () > 290 or head.xcor() < -290 or head.ycor () > 290 or head.ycor () < -290:
        time.sleep(1.5)
        head.goto (0,0)
        head.direction = "stop"

        # Skrytí částí těla
        for one_body_part in body_parts:
            one_body_part.goto (1500,1500)
        
        # PO kolizi vyprázdníme list s částmi těla
        body_parts.clear ()

        # Reset skore
        score = 0
        score_sign.clear()
        score_sign.write (f"Skóre: {score}   Nejvyšší skóre: {highest_score}", align="center", font=18)
        
    # Kolize hlavy s jablkem
    if head.distance (apple) < 20:
        x = random.randint (-270, 270)
        y = random.randint (-270, 270)
        apple.goto(x, y)
        
        # Přidání části těla
        new_body_part = Turtle ("square")
        new_body_part.speed = 0
        new_body_part.color ("grey")
        new_body_part.penup ()
        body_parts.append (new_body_part)

        # Zvýšení skore
        score += 10

        if score > highest_score:
            highest_score = score
        
        score_sign.clear()
        score_sign.write (f"Skóre: {score}   Nejvyšší skóre: {highest_score}", align="center", font=18)

    for index in range(len(body_parts) -1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)


    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)

    move()

    # Kontrola kolize hlavy s tělem
    for one_body_part in body_parts:
        if one_body_part.distance (head) < 20:
            time.sleep(1.5)
            head.goto (0,0)
            head.direction = "stop"
            
            
            # Skrytí částí těla
            for one_body_part in body_parts:
                one_body_part.goto (1500,1500)
        
            # PO kolizi vyprázdníme list s částmi těla
            body_parts.clear ()
            # Reset skore
            score = 0
            score_sign.clear()
            score_sign.write (f"Skóre: {score}   Nejvyšší skóre: {highest_score}", align="center", font=18)



    time.sleep(0.3)
    
screen.exitonclick()





