import turtle   # oyunun oynanacağı ekranın kütüphanesi
import time
import random
game_screen = turtle.Screen()
game_screen.title("Snake Game")
game_screen.setup(width=1400, height=800)  # oyun ekranının büyüklüğü
game_screen.bgcolor('orange')   # oyun ekranı rengi
game_screen.tracer(0)     # pencerenin sürekli tekrar etmemesini sağladık.

snake_head = turtle.Turtle()  # yılanın kafası
snake_head.speed(0)  # yılanın başlangıç hızı
snake_head.color('black')  # yılanın rengi
snake_head.shape('circle')  # yılanın şekli
snake_head.penup()
snake_head.goto(0, 0)   # yılanın başlama noktası merkez.
snake_head.direction = 'stop'    # yılanın başlangıçta durması

snake_speed = 0.1

bait = turtle.Turtle()  # yılan için yem oluşturuyoruz.
bait.speed(0)
bait.color('red')
bait.shape('circle')
bait.penup()
bait.goto(0, 100)  # yemin başlangıç konumu
bait.shapesize(0.80, 0.80)   # yemin boyutu

tail = []
score = 0
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color('white')
score_board.shape('square')
score_board.penup()
score_board.goto(0, 350)
score_board.hideturtle()
score_board.write('Score : {}'.format(score), align='center',
                  font=('Courier', 30, 'normal'))


def move():   # yılanın hareket fonksiyonu
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 10)
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 10)
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 10)
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 10)


def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'


def down_up():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'


def right_up():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'


def left_up():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'


game_screen.listen()
game_screen.onkey(go_up, 'Up')  # klavye hareketleri
game_screen.onkey(down_up, 'Down')
game_screen.onkey(left_up, 'Left')
game_screen.onkey(right_up, 'Right')
while True:
    game_screen.update()

    # yılan kordinatlar dışına çıkarsa oyun biter
    if snake_head.xcor() > 700 or snake_head.xcor() < -700 or snake_head.ycor() > 400 or snake_head.ycor() < -400:
        time.sleep(1)
        snake_head.goto(0, 0)  # konumu 0 yapar
        snake_head.direction = 'stop'

        for i in tail:  # kuyrukları pencere dışına atar
            i.goto(5000, 5000)

        tail = []
        score = 0
        score_board.clear()
        score_board.write('Score : {}'.format(score),
                          align='center', font=('Courier', 30, 'normal'))
        snake_speed = 0.1

    if snake_head.distance(bait) < 20:  # yemi yiyip random konum oluşturuyor
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        bait.goto(x, y)

        score += 10  # skore ayarı yaptık
        score_board.clear()
        score_board.write('Score : {}'.format(score),
                          align='center', font=('Courier', 30, 'normal'))
        snake_speed = snake_speed - 0.01

        add_tail = turtle.Turtle()  # kuyruğu ekledik
        add_tail.speed(0)
        add_tail.shape('circle')
        add_tail.color('black')
        add_tail.penup()
        tail.append(add_tail)

    for i in range(len(tail) - 1, 0, -1):  # kuyruğun yılanı takip etmesini sağladık
        x = tail[i-1].xcor()
        y = tail[i-1].ycor()

        tail[i].goto(x, y)

    if len(tail) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        tail[0].goto(x, y)

    move()
    time.sleep(snake_speed)
