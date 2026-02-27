import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Fungsi persegi panjang
def persegi_panjang(panjang, lebar):
    for i in range(2):
        t.forward(panjang)
        t.right(90)
        t.forward(lebar)
        t.right(90)

# Fungsi segitiga (sama sisi)
def segitiga(sisi):
    for i in range(3):
        t.forward(sisi)
        t.left(120)

# Fungsi trapesium
def trapesium(a, b, tinggi):
    t.forward(a)
    t.left(120)
    t.forward(tinggi)
    t.left(60)
    t.forward(b)
    t.left(60)
    t.forward(tinggi)
    t.left(120)

# Fungsi jajar genjang
def jajar_genjang(panjang, sisi_miring):
    t.forward(panjang)
    t.left(60)
    t.forward(sisi_miring)
    t.left(120)
    t.forward(panjang)
    t.left(60)
    t.forward(sisi_miring)
    t.left(120)

# Fungsi belah ketupat
def belah_ketupat(sisi):
    for i in range(2):
        t.forward(sisi)
        t.left(60)
        t.forward(sisi)
        t.left(120)

# Gambar bangun-bangun

# Persegi panjang
t.penup()
t.goto(-300, 100)
t.pendown()
persegi_panjang(120, 60)

# Segitiga
t.penup()
t.goto(-100, 100)
t.pendown()
segitiga(100)

# Trapesium
t.penup()
t.goto(100, 100)
t.pendown()
trapesium(120, 60, 80)

# Jajar genjang
t.penup()
t.goto(-200, -100)
t.pendown()
jajar_genjang(120, 80)

# Belah ketupat
t.penup()
t.goto(100, -100)
t.pendown()
belah_ketupat(80)

turtle.done()