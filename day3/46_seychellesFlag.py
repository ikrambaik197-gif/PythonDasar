import turtle

def drawRectangle(ttl, x, y, width, height):
    """ Draw a rectangle of dimensions width and height """
    ttl.up()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.down()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.up()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.penup()

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

# Set up screen
turtle.setup(1500, 1000, 0, 0)
myBlue = "#003882"
myYellow = "#FCD647"
myRed = "#D12421"
myWhite = "#FFFFFF"
myGreen = "#007336"

Joe = turtle.Turtle()
# Gunakan mode warna 255 jika ingin input RGB manual, 
# tapi karena kita pakai Hex string, biarkan default atau pastikan Turtle siap.
Joe.speed(0) 

# Gambar bingkai luar
drawRectangle(Joe, 0, 300, 600, 300)

# Titik pusat semua segitiga ada di (0,0)
Joe.goto(0, 0)

# 1. Segitiga Biru
fillTriangle(Joe, 0, 0, 0, 300, 200, 300, myBlue)
# 2. Segitiga Kuning
fillTriangle(Joe, 0, 0, 200, 300, 400, 300, myYellow)
# 3. Segitiga Merah
fillTriangle(Joe, 0, 0, 400, 300, 600, 300, myRed)
# 4. Segitiga Putih
fillTriangle(Joe, 0, 0, 600, 300, 600, 150, myWhite)
# 5. Segitiga Hijau
fillTriangle(Joe, 0, 0, 600, 150, 600, 0, myGreen)

Joe.hideturtle()
turtle.done()