from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color
#import keyboard


class PongPaddle(Widget):
    score = NumericProperty(0)
    Color = ListProperty((1,1,1,1))

    # ball bounce off of paddles
    def bounce_ball(self, ball):
        if self.collide_widget(ball):   
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            if (vx * 1.1) < 10:
                vel = bounced * 1.1
                ball.velocity = vel.x, vel.y + offset
            else:
                vel = bounced
                ball.velocity = vel.x, vel.y + offset
            return True
        else:
            return False
    
    # moving paddles with keyboard
    def move_paddles(self, player):
        if player == 1:
            #if keyboard.is_pressed("w"):
                #self.y += 5
            #if keyboard.is_pressed("s"):
                #self.y -= 5
            pass
        else:
            #if keyboard.is_pressed("up"):
                #self.y += 5
            #if keyboard.is_pressed("down"):
                #self.y -= 5
            pass


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    Color = ListProperty((1, 1, 1, 1))

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()
        #print(self.ball.velocity)

        self.player1.Color = (0, (135/255), (130/255), 1) 
        self.player2.Color = ( (199/255),1, (145/255),1)

        # keyboard
        self.player1.move_paddles(1)
        self.player2.move_paddles(2)

        # bounce of paddles
        if self.player1.bounce_ball(self.ball):
            self.ball.Color = (0, (135/255), (130/255), 1)

        if self.player2.bounce_ball(self.ball):
            self.ball.Color = ( (199/255),1, (145/255),1)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # score
        if (self.ball.x + 25) < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
            #self.ball.Color = (68/255, 214/255, 44/255, 1) 
            
        if (self.ball.right - 25) > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
            #self.ball.Color = (68/255, 214/255, 44/255, 1) 

    # moving paddles with mouse/trackpad
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()