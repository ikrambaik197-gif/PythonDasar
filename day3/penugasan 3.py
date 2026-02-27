import turtle

# Setup layar
screen = turtle.Screen()
screen.title("Bendera Indonesia")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Ukuran bendera
panjang = 300
tinggi = 200

# Pindah ke posisi awal
t.penup()
t.goto(-150, 100)
t.pendown()

# Bagian merah (atas)
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(panjang)
    t.right(90)
    t.forward(tinggi/2)
    t.right(90)
t.end_fill()

# Pindah ke bagian putih (bawah)
t.right(90)
t.forward(tinggi/2)
t.left(90)

# Bagian putih (bawah)
t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.forward(panjang)
    t.right(90)
    t.forward(tinggi/2)
    t.right(90)
t.end_fill()

turtle.done()