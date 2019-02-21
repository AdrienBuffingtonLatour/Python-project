# Use arrows on keyboard to move player and space bar to shoot a missile #
# Your score is displayed on the upper left corner #
# Do not collide with an enemy spaceship or an asteroid #
# You have 3 lives #

import turtle
import random
import math

# Create Screen and register shapes
wn = turtle.Screen()
wn.setup(height=1000, width=1000, startx=0, starty=0)
wn.bgcolor("black")
wn.title("Final Project")
wn.register_shape("star", ((100, 10), (40, 198), (190, 78), (10, 78), (160, 198)))
# Speed up drawing
wn.tracer(3)

# Create main class of Spaceship


class Spaceship(turtle.Turtle):

    def __init__(self, shape, color, startx, starty):
        super().__init__()  # calling parent turtle.Turtle class
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.shape(shape)
        self.color(color)
        self.goto(startx, starty)
        self.showturtle()

    def collision(self, another_spaceship):
        diffX = self.xcor() - another_spaceship.xcor()
        diffY = self.ycor() - another_spaceship.ycor()
        distance = math.sqrt(diffX ** 2 + diffY ** 2)
        if distance < 20:
            return True
        else:
            return False

    def move(self):
        self.forward(3)


class Player(Spaceship):

    def __init__(self, shape, color, startx, starty):
        super().__init__(shape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=0.8, outline=None)

    def go_up(self):
        y = self.ycor() + 15
        self.sety(y)
        if self.ycor() > 299:
            self.sety(290)

    def go_down(self):
        y = self.ycor() - 15
        self.sety(y)
        if self.ycor() < -290:
            self.sety(-290)

    def go_left(self):
        x = self.xcor() - 15
        self.setx(x)
        if self.xcor() < -290:
            self.setx(-290)

    def go_right(self):
        x = self.xcor() + 15
        self.setx(x)
        if self.xcor() > 290:
            self.setx(290)


class Ennemy(Spaceship):

    def __init__(self, shape, color, startx, starty):
        super().__init__(shape, color, startx, starty)
        self.hideturtle()
        self.left(180)
        self.showturtle()

    def collision_border(self):
        if abs(self.xcor()) > 300 or abs(self.ycor()) > 300:
            self.hideturtle()
            self.up()
            self.setposition(290, random.randint(-290, 290))
            self.showturtle()


class Game(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.score = 0
        self.lives = 99

    def border(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-300, -300)
        self.pendown()
        for i in range(4):
            self.forward(600)
            self.left(90)


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.score = 0

    def show_score(self):
        self.hideturtle()
        self.up()
        self.setposition(-400, 250)
        self.color("white")
        self.write("Score: {}".format(0))

    def update_score(self):
        self.undo()
        self.hideturtle()
        self.up()
        self.setposition(-400, 250)
        self.color("white")
        self.write("Score: {}".format(self.score))

    def lose(self):
        wn.clear()
        wn.bgcolor("black")
        self.setposition(0, 0)
        self.color("white")
        self.write("Sorry, you lose."'\n'  "Your score: {} points".format(self.score), False, align="center",
                         font=("Arial", 16, "normal"))


class Lives(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.lives = 3

    def show_lives(self):
        self.hideturtle()
        self.up()
        self.setposition(-400, 200)
        self.color("white")
        self.write("Lives: {}".format(self.lives))

    def update_lives(self):
        self.undo()
        self.hideturtle()
        self.up()
        self.setposition(-400, 200)
        self.color("white")
        self.write("Lives: {}".format(self.lives))


class Projectile(Spaceship):

    def __init__(self, shape, color, startx, starty):
        super().__init__(shape, color, startx, starty)
        self.shapesize(stretch_wid=0.4, stretch_len=0.6, outline=None)
        self.status = "ready"
        self.hideturtle()

    def fire(self):
        if self.status == "ready":
            self.status = "firing"
            x = player.xcor()
            y = player.ycor()
            self.setposition(x, y)

    def move_bullet(self):
        if self.status == "firing":
            self.showturtle()
            self.forward(9)
        if abs(self.xcor()) > 300 or abs(self.ycor()) > 300:
            self.hideturtle()
            self.setposition(-900, -900)
            self.status = "ready"


class Star(Spaceship):

    def __init__(self, shape, color, startx, starty):
        super().__init__(shape, color, startx, starty)
        self.shapesize(0.1)
        self.hideturtle()
        self.left(random.choice((90, 270)))
        self.showturtle()

    def collision_border(self):
        if abs(self.ycor()) > 295 or abs(self.xcor()) > 295:
            self.setposition(random.randint(-294, 294), random.choice((-294, 294)))
            if self.ycor() > 291:
                self.setheading(270)
            if self.ycor() < -291:
                self.setheading(90)


# Creating instances

game = Game()
game.border()

score = Score()
score.show_score()

lives = Lives()
lives.show_lives()

player = Player("triangle", "blue", 0, -100)

projectile = Projectile("triangle", "white", -900, -900)

# Create multiple ennemies and stars

ennemies = []
for i in range(10):
    ennemies.append(Ennemy("triangle", "red", random.randint(-290, 290), random.randint(-290, 290)))

stars = []
for i in range(5):
    stars.append(Star("star", "yellow", random.randint(-295, 295), random.choice((-295, 295))))

# Keyboard Bindings

wn.listen()
wn.onkeypress(player.go_up, "Up")
wn.onkeypress(player.go_down, "Down")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(projectile.fire, "space")

# Game loop

playing = True

while playing:
    wn.update()
    projectile.move_bullet()

    for ennemy in ennemies:
        ennemy.move()
        ennemy.collision_border()
        if projectile.collision(ennemy):
            score.score += 1
            projectile.hideturtle()
            projectile.goto(-900, -900)
            x = 290
            y = random.randint(-290, 290)
            ennemy.goto(x, y)
            score.update_score()

        if player.collision(ennemy):
            lives.lives -= 1
            x = 290
            y = random.randint(-290, 290)
            ennemy.hideturtle()
            ennemy.goto(x, y)
            ennemy.showturtle()
            lives.update_lives()

    for star in stars:
        star.move()
        star.collision_border()
        if star.collision(player):
            lives.lives -= 1
            star.hideturtle()
            star.setposition(random.randint(-290, 290), random.choice((-290, 290)))
            star.showturtle()
            lives.update_lives()

    if lives.lives == 0:
        playing = False

score.lose()

wn.mainloop()
