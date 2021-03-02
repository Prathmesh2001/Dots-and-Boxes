from tkinter import *

rows, cols = (65, 65)
matrix = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(0)
    matrix.append(col)
queue = []
user = 1
flag=[0,0]
red_count = 0
blue_count = 0



# select user chance
def user_chance(event):
    global user
    change = 0
    x_coordinate = event.x
    y_coordinate = event.y
    for i in range(8):
        for j in range(8):

            if y_coordinate >= offset * i + margin - 2 and y_coordinate <= offset * i + margin + dotsize + 2:
                if x_coordinate >= offset * j + margin + dotsize / 2 and x_coordinate <= offset * (
                        j + 1) + margin + dotsize / 2 and j != 7:
                    dot_1 = j + i * 8 + 1
                    dot_2 = j + i * 8 + 2
                    change = 1
            if x_coordinate >= offset * i + margin - 2 and x_coordinate <= offset * i + margin + dotsize + 2:
                if y_coordinate >= offset * j + margin + dotsize / 2 and y_coordinate <= offset * (
                        j + 1) + margin + dotsize / 2 and j != 7:
                    dot_1 = i + j * 8 + 1
                    dot_2 = i + j * 8 + 9
                    change = 1
    if change != 0 and matrix[dot_1][dot_2]!=1:
        # l10=Label(f2,text="Player 1 turn")
        if user == 1:
            l4.config(text="PLAYER 2 TURN !!!", fg="red")
            l4.pack()
        else:
            l4.config(text="PLAYER 1 TURN !!!", fg="blue")
            l4.pack()

        print(user)
        make_line(x_coordinate, y_coordinate)


# make lines between dots
def make_line(x_coordinate, y_coordinate):
    global user, change
    change = 0
    m = 0
    for i in range(8):
        for j in range(8):

            if y_coordinate >= offset * i + margin - 2 and y_coordinate <= offset * i + margin + dotsize + 2:
                if x_coordinate >= offset * j + margin + dotsize / 2 and x_coordinate <= offset * (
                        j + 1) + margin + dotsize / 2 and j != 7:
                    can_widget.create_line(offset * j + margin + dotsize / 2,
                                           offset * i + margin + dotsize / 2,
                                           offset * (j + 1) + margin + dotsize / 2,
                                           offset * i + margin + dotsize / 2)
                    dot_1 = j + i * 8 + 1
                    dot_2 = j + i * 8 + 2
                    m = m + 1
                    break
            if x_coordinate >= offset * i + margin - 2 and x_coordinate <= offset * i + margin + dotsize + 2:
                if y_coordinate >= offset * j + margin + dotsize / 2 and y_coordinate <= offset * (
                        j + 1) + margin + dotsize / 2 and j != 7:
                    can_widget.create_line(offset * i + margin + dotsize / 2,
                                           offset * j + margin + dotsize / 2,
                                           offset * i + margin + dotsize / 2,
                                           offset * (j + 1) + margin + dotsize / 2)
                    dot_1 = i + j * 8 + 1
                    dot_2 = i + j * 8 + 9
                    m = m + 1
                    break
        if m != 0:
            break
    if m != 0:
        if flag[user - 1] == 1:
            flag[user - 1] = 0
        if user == 1:
            user = 2
        else:
            user = 1
        check_box(dot_1, dot_2)


# check if box is formed or not
def check_box(x, y):
    matrix[x][y] = 1
    matrix[y][x] = 1
    diff = y - x
    if diff == 1:
        opposite = -8
        traverse(diff, opposite, x, y)
        opposite = 8
        traverse(diff, opposite, x, y)
    elif diff == 8:
        opposite = -1
        traverse(diff, opposite, x, y)
        opposite = 1
        traverse(diff, opposite, x, y)


# for traversing the path
def traverse(a, b, c, d):
    global user
    m = 0
    queue.append(c)
    X = c + b
    if X > 0 and X < 65:
        if matrix[c][X] == 1:
            queue.append(X)
            if matrix[X][X + a] == 1:
                X = X + a
                queue.append(X)
                if matrix[X][X - b] == 1:
                    X = X - b
                    queue.append(X)
                    m = 1
    if m == 1:
        if user == 1:
            user = 2
        else:
            user = 1
        if user == 1:
            l4.config(text="PLAYER 1 TURN !!!", fg="blue")
            l4.pack()
        else:
            l4.config(text="PLAYER 2 TURN !!!", fg="red")
            l4.pack()
        print(user)
        flag[user-1]=0
        user_color()

    del queue[0:]



def user_color():
    global red_count,blue_count
    a = queue[3]
    b = queue[1]
    if user == 1:
        color = "SteelBlue2"
        blue_count += 1
        l2.config(text=f"Player 1: {blue_count}")
        l2.pack()
    else:
        color = "firebrick1"
        red_count += 1
        l3.config(text=f"Player 2: {red_count}")
        l3.pack()
    if a % 8 != 0:
        x1 = (a % 8 - 1) * offset + margin + dotsize / 2
    else:
        x1 = 7 * offset + margin + dotsize / 2
    y1 = int(a / 8.1) * offset + margin + dotsize / 2
    if b % 8 != 0:
        x2 = (b % 8 - 1) * offset + margin + dotsize / 2
    else:
        x2 = 7 * offset + margin + dotsize / 2
    y2 = int(b / 8.1) * offset + margin + dotsize / 2
    print(f"{x1},{y1}")
    can_widget.create_rectangle(x1, y1, x2, y2, fill=color)


root = Tk()

canvas_width = 600
canvas_height = 500
offset = 40
margin = 50
dotsize = 5

root.geometry("600x450")
#restrict the height
root.resizable(width=False,height=False)

root.title("Dots and Boxes - (Game)")

f1 = Frame(root, bg="coral",borderwidth=5, relief = SUNKEN)
f1.pack(side = RIGHT, padx=5,pady=5,fill="y", anchor = NE)

f2 = Frame(root, bg="OliveDrab1",borderwidth=5, relief = RIDGE)
f2.pack(side = TOP, padx=5, fill="x", anchor = N)

l4=Label(f2,text="PLAYER 1 TURN !!!",font="Verdana 10",fg="blue",bg="OliveDrab1")
l4.pack(padx=10)

l1 = Label(f1, text="Players:-", font="Verdana 20 bold",fg="white",bg="coral",padx=10)
l1.pack(pady=20)

score1 = "Player 1: 0"
l2 = Label(f1, text=score1,font="Verdana 12",borderwidth=5,relief="ridge",fg="blue", bg="azure2",padx=3,pady=3)
l2.pack(pady=15)

score2 = "Player 2: 0"
l3 = Label(f1, text=score2,font="Verdana 12",borderwidth=5,relief="ridge",fg="red", bg="azure2",padx=3,pady=3)
l3.pack(pady=15)

#create canvas
can_widget = Canvas(root, width=canvas_width, height = canvas_height, bg="azure2",borderwidth=3, relief = SOLID)
can_widget.pack(pady=5,padx=5)

#Bind canvas
can_widget.bind("<Button-1>",user_chance)

#can_widget.create_rectangle(offset+ margin+ dotsize/2,offset+ margin+ dotsize/2,x2,y2,fill="black")


#dots plotting
for i in range(8):
        for j in range(8):
            can_widget.create_oval(offset*i+ margin,
                       offset*j+ margin,
                       offset*i+ margin+ dotsize,
                       offset*j+ margin+ dotsize,
                       fill="black"
                       )





root.mainloop()
