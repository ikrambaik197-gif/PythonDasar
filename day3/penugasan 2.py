import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(4)
t.pensize(2)

# Fungsi persegi panjang
def persegi_panjang(panjang, lebar, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(2):
        t.forward(panjang)
        t.right(90)
        t.forward(lebar)
        t.right(90)
    t.end_fill()

# Fungsi segitiga
def segitiga(sisi, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(3):
        t.forward(sisi)
        t.left(120)
    t.end_fill()

# Fungsi trapesium
def trapesium(a, b, tinggi, warna):
    t.fillcolor(warna)
    t.begin_fill()
    t.forward(a)
    t.left(120)
    t.forward(tinggi)
    t.left(60)
    t.forward(b)
    t.left(60)
    t.forward(tinggi)
    t.left(120)
    t.end_fill()

# Fungsi jajar genjang
def jajar_genjang(panjang, sisi_miring, warna):
    t.fillcolor(warna)
    t.begin_fill()
    t.forward(panjang)
    t.left(60)
    t.forward(sisi_miring)
    t.left(120)
    t.forward(panjang)
    t.left(60)
    t.forward(sisi_miring)
    t.left(120)
    t.end_fill()

# Fungsi segilima
def segilima(sisi, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(5):
        t.forward(sisi)
        t.left(72)
    t.end_fill()

# Gambar bangun-bangun

# Persegi panjang (merah)
t.penup()
t.goto(-300, 100)
t.pendown()
persegi_panjang(120, 70, "red")

# Segitiga (kuning)
t.penup()
t.goto(-100, 100)
t.pendown()
segitiga(100, "yellow")

# Trapesium (hijau)
t.penup()
t.goto(100, 100)
t.pendown()
trapesium(140, 80, 80, "green")

# Jajar genjang (biru)
t.penup()
t.goto(-200, -100)
t.pendown()
jajar_genjang(120, 80, "blue")

# Segilima (ungu)
t.penup()
t.goto(100, -100)
t.pendown()
segilima(80, "purple")

turtle.done()