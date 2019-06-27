import pyglet
import resources
import math
import time
import random


class Ball(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity = 400
        self.rotate(random.choice((5, 355, 175, 185)))
        self.key_handler = pyglet.window.key.KeyStateHandler()


    def update(self, dt):
        self.x += self.velocity_x * dt  # move ball based on its velocity
        self.y += self.velocity_y * dt
        self.check_collision()  # check for collisions with bounds/players

        # keys to change ball velocity
        if self.key_handler[pyglet.window.key._1]:
            self.velocity = 100
            self.rotate(self.rotation)  # update velocity components
        elif self.key_handler[pyglet.window.key._2]:
            self.velocity = 200
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._3]:
            self.velocity = 300
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._4]:
            self.velocity = 400
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._5]:
            self.velocity = 500
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._6]:
            self.velocity = 600
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._7]:
            self.velocity = 700
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._8]:
            self.velocity = 800
            self.rotate(self.rotation)
        elif self.key_handler[pyglet.window.key._9]:
            self.velocity = 900
            self.rotate(self.rotation)


    def rotate(self, rotation):
        self.rotation = rotation
        angle_radians = -math.radians(self.rotation)  # convert to radians
        self.velocity_x = self.velocity * math.cos(angle_radians)  # recalculate x velocity component
        self.velocity_y = self.velocity * math.sin(angle_radians)  # recalculate y velocity component

    def check_collision(self):
        # check upper and bottom bounds
        if self.y <= (self.image.width*self.scale)/2:  # bottom
            self.rotate(360 - self.rotation)
        elif self.y >= window.height - (self.image.width*self.scale)/2:  # upper
            self.rotate(360 - self.rotation)

        # check left and right bounds
        if self.x <= player1.x + (self.image.width*self.scale)/2:  # left
            if abs(self.y - player1.y) <= (player1.image.height*player1.scale)/2 + (self.image.height*ball.scale)/2:
                # new rotation is based on hit location and hit angle
                self.rotate((self.y - player1.y) / (((player1.image.height*player1.scale)/20)) * ((180 - self.rotation)%360))
                #self.rotate((self.y - player1.y) / (((player1.image.height*player1.scale)/2)) * 90)

            else:  # player 2 gains point
                player2.score += 1
                score_label.text = str(player1.score) + " : " + str(player2.score)
                pyglet.clock.unschedule(update)
                pause_label.text = "GOAL!"
                time.sleep(1)
                pyglet.clock.schedule_interval(update, 1 / 120)
                pause_label.text = ""
                self.x, self.y = window.width/2, window.height/2
                self.rotate(random.choice((5, 355)))
        elif self.x >= player2.x - (self.image.width*self.scale)/2:  # right
            if abs(self.y - player2.y) <= (player2.image.height*player2.scale)/2  + (self.image.height*ball.scale)/2:
                # new rotation is based on hit location and hit angle
                self.rotate(180 + ((self.y - player2.y) / ((player2.image.height*player2.scale)/20)) * (self.rotation%360))
            else: # player 1 gains point
                player1.score += 1
                score_label.text = str(player1.score) + " : " + str(player2.score)
                pyglet.clock.unschedule(update)
                pause_label.text = "GOAL!"
                time.sleep(1)
                pyglet.clock.schedule_interval(update, 1 / 120)
                pause_label.text = ""
                self.x, self.y = window.width/2, window.height/2
                self.rotate(random.choice((175, 185)))


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.velocity_y = 0
        self.score = 0

    def move_up(self):
        if self.y < window.height - self.image.width/2:
            self.velocity_y = 500
        else:
            self.velocity_y = 0
    def move_down(self):
        if self.y > self.image.width/2:
            self.velocity_y = -500
        else:
            self.velocity_y = 0

    def update(self, dt):
        if self.key_handler[pyglet.window.key.UP]:
            self.move_up()
        elif self.key_handler[pyglet.window.key.DOWN] and self.y > self.image.width/2:
            self.move_down()
        else:
            self.velocity_y = 0

        self.y += self.velocity_y * dt

class ComputerPlayer(pyglet.sprite.Sprite):
    global arrived
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_y = 500
        self.score = 0

    def move_up(self):
        if self.y < window.height - self.image.width / 2:
            self.velocity_y = 500
        else:
            self.velocity_y = 0

    def move_down(self):
        if self.y > self.image.width / 2:
            self.velocity_y = -500
        else:
            self.velocity_y = 0

    def update(self, dt):

        # move schemes for different difficulty levels
        if ai_player == 0:  # 0 - human (using mouse)
            if abs(destination - self.y) > 10:
                if destination > self.y:
                    self.move_up()
                else:
                    self.move_down()
            else:
                self.velocity_y = 0
        elif ai_player == 1:  # random moves
            if random.randint(1, 20) == 1:
                if self.velocity_y > 0:
                    self.move_down()
                elif self.velocity_y < 0:
                    self.move_up()
                else:
                    if random.randint(1, 2) == 1:
                        self.move_up()
                    else:
                        self.move_down()
            else:
                if self.velocity_y > 0:
                    self.move_up()
                elif self.velocity_y < 0:
                    self.move_down()
                else:
                    if random.randint(1, 2) == 1:
                        self.move_up()
                    else:
                        self.move_down()
        elif ai_player == 2:  # following ball y - slower version
            if random.randint(1, 3) == 1:
                if ball.y > self.y:
                    self.move_up()
                elif ball.y < self.y:
                    self.move_down()
                else:
                    self.velocity_y = 0
            else:
                self.velocity_y = 0
        elif ai_player == 3:  # following ball y - faster version
            if ball.y > self.y:
                self.move_up()
            elif ball.y < self.y:
                self.move_down()
            else:
                self.velocity_y = 0

        self.y += self.velocity_y * dt


#--------------------------------------------------main-----------------------------------------------------------------

config = open("config.txt").readlines()  # load file with configuration
for i in range(len(config)):
    config[i] = config[i].replace("\n", "")
    config[i] = config[i].split()
    config[i] = int(config[i][1])

window_x, window_y, fullscreen, mouse_visible, ai_player = config  # ai_player - computer player difficulty (0 - 3) (0 = human player)

window = pyglet.window.Window(window_x, window_y)  # set up a window
if fullscreen:
    window.set_fullscreen()

if mouse_visible:
    window.set_mouse_visible(True)
else:
    window.set_mouse_visible(False)

main_batch = pyglet.graphics.Batch()  # all sprites and labels that are drawn on start are in main_batch
pause_enabled = True

player1 = Player(resources.player_image, window.width*0.1, window.height/2, batch=main_batch)
player1.scale = 0.1

player2 = ComputerPlayer(resources.player_image, window.width*0.9, window.height/2, batch=main_batch)
player2.scale = 0.1
destination = window.height/2  # mouse localisation - destination for human player 2

ball = Ball(resources.ball_image, window.width/2, window.height/2, batch=main_batch)
ball.scale = 0.1

score_label = pyglet.text.Label(str(player1.score) + " : " + str(player2.score), font_size=40,
                                x=window.width/2, y=window.height*0.9, batch=main_batch, anchor_x = "center", bold=True)

pause_label = pyglet.text.Label("press space to start, h for help", x=window.width/2, y=window.height/2 + 20,
                                batch=main_batch, anchor_x = "center", bold=True, font_size=20)

help_label = pyglet.text.Label("", x=window.width/2, y=window.height*0.4, batch=main_batch,
                               anchor_x = "center", width=window.width-40, multiline=True)

def update(dt):  # update sprite, check if someone wins
    global pause_enabled
    ball.update(dt)
    player1.update(dt)
    player2.update(dt)
    if player1.score >= 10:
        pause_enabled = False
        pyglet.clock.unschedule(update)
        pause_label.text = "Player 1 wins!"
    elif player2.score >= 10:
        pause_enabled = False
        pyglet.clock.unschedule(update)
        pause_label.text = "Player 2 wins!"


@window.event
def on_draw():
    window.clear()
    main_batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    global ai_player
    global pause_enabled

    if symbol == pyglet.window.key.SPACE and pause_enabled:  # pause/unpause game
        if pause_label.text:
            pyglet.clock.schedule_interval(update, 1 / 120) # call update() 120 times per second (game is running)
            pause_label.text = ""
        else:
            pyglet.clock.unschedule(update)  # stop calling update() (game stops)
            pause_label.text = "PAUSED"

    if symbol == pyglet.window.key.H:  # display/hide help message
        if help_label.text:
            help_label.text = ""
        else:
            help_label.text = "Controls:\nPlayer 1: use up and down arrow to move\n" \
                              "Player 2: use mouse to move\n\nGeneral:\n" \
                              "space - pause/unpause, r - restart, 1-9 - change ball speed, h - show/hide this messsage, " \
                              "NUMPAD 0 - play vs. human, NUMPAD 1-3 - play vs. computer (difficulty 1-3)" \
                              "\n\nGood luck and have fun!"

    if symbol == pyglet.window.key.R:  # restart game
        player1.score, player1.x, player1.y, player1.velocity_y = 0, window.width*0.1, window.height/2, 0
        player2.score, player2.x, player2.y, player2.velocity_y = 0, window.width*0.9, window.height/2, 0
        ball.x, ball.y = window.width/2, window.height/2
        ball.rotate(random.choice((5, 355, 175, 185)))
        score_label.text = str(player1.score) + " : " + str(player2.score)
        pause_enabled = True  # enable pause (required after end of match)

        if pause_label.text:
            pyglet.clock.schedule_interval(update, 1 / 120)  # call update() 120 times per second
            pause_label.text = ""

    # difficulty control
    if symbol == pyglet.window.key.NUM_0:
        ai_player = 0
    if symbol == pyglet.window.key.NUM_1:
        ai_player = 1
    if symbol == pyglet.window.key.NUM_2:
        ai_player = 2
    if symbol == pyglet.window.key.NUM_3:
        ai_player = 3

@window.event
def on_mouse_motion(x, y, dx, dy):
    global destination
    destination = y

window.push_handlers(player1)
window.push_handlers(player1.key_handler)
window.push_handlers(ball)
window.push_handlers(ball.key_handler)

pyglet.app.run()