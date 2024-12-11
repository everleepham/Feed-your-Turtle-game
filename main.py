import turtle
import random
import time

# create screen
game = turtle.Screen()
game.title("Feed your turtle!")
game.bgcolor("#9acd32")
game.setup(width=600, height=600)

# create player
player = turtle.Turtle()
player.shape("turtle")
player.color("#006400")
player.shapesize(stretch_wid=2, stretch_len=2)
player.penup()
player.speed(0)

# create food (small turtle)
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("#8b0000")
food.penup()
food.goto(0,100)

bombs = []

# create bombs
def create_bomb():
    bomb = turtle.Turtle()
    bomb.speed(0)
    bomb.shape("circle")
    bomb.color("black")
    bomb.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    bomb.goto(x, y)
    bombs.append(bomb)

# create a loop that generate bombs
num_bombs = 10
for i in range(num_bombs):
    create_bomb()

# set time, speed
score = 0
time_limit = 60
start_time = time.time()
speed = 20

# set keyboard interact
def up():
    y = player.ycor()
    if y < game.window_height() / 2 - 20: # create limit to keep the turtle on screen 
        player.sety(y + speed)

def down():
    y = player.ycor()
    if y > -game.window_height() / 2 + 20:
        player.sety(y - speed)

def left():
    x = player.xcor()
    if x > -game.window_width() / 2 + 20:
        player.setx(x - speed)

def right():
    x = player.xcor()
    if x < game.window_width() / 2 - 20:
        player.setx(x + speed)

def start_game():
    global score, start_time
    score = 0
    start_time = time.time()
    reset_game()

def end_game():
    global score
    show_score()
    reset_game()

def reset_game():
    global score
    player.goto(0, 0)
    player.setheading(0)
    game.title(f"Feed your turtle! - Score: {score} - Time Left: {int(time_limit)}s")

def show_score():
    global score
    end_message = f"Feed your turtle! - Final Score: {score}"
    game.title(end_message)
    player_name = turtle.textinput("Game Over!", end_message + "\nEnter your name:")
    print(f"Player: {player_name}, Score: {score}")

game.listen()
game.onkeypress(up, "Up")
game.onkeypress(down, "Down")
game.onkeypress(left, "Left")
game.onkeypress(right, "Right")

fall_speed = 4
while time.time() - start_time < time_limit:
    # get point if player touches foods
    if player.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        score += 1

    # bombs fall
    for bomb in bombs:
        y = bomb.ycor()
        y -= fall_speed
        bomb.sety(y) 

    # minus score if player touches bomb
        if player.distance(bomb) < 20:
            score -= 1
            bomb.goto(random.randint(-290, 290), random.randint(150, 290))
        if y < -290:
            bomb.goto(random.randint(-290, 290), random.randint(100, 290))

    # create more bombs
    if random.random() < 0.01:
        create_bomb()

    game.title(f"Feed your turtle! - Score: {score} - Time Left: {int(time_limit - (time.time() - start_time))}s")
    game.update()

end_game()
turtle.done()
