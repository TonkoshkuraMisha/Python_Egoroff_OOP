from tkinter import *
def Call():
    msg = Label(window, text = "You pressed the button")
    msg.place(x = 80, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"
window = Tk()
window.geometry("300x300")
button = Button(text = "Press me", command = Call)
button.place(x = 90, y = 20, width = 120, height = 25)
window.mainloop()


from tkinter import *
def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message
window = Tk()
window.geometry("500x200")
label1 = Label(text = "Enter your name: ")
label1.place(x = 30, y = 20)
textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 20, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()
button1 = Button(text = "Press me", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)
textbox2 = Message(text = "")
textbox2.place(x = 150, y = 50, width = 200, height = 25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"
window.mainloop()

from tkinter import *


def add_on():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num + answer
    output_txt["text"] = total


def reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()


total = 0
num = 0
window = Tk()
window.title("Adding Together")
window.geometry("450x100")
enter_lbl = Label(text="Enter a number:")
enter_lbl.place(x=50, y=20, width=100, height=25)
enter_txt = Entry(text=0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"] = "center"
enter_txt.focus()
add_btn = Button(text="Add", command=add_on)
add_btn.place(x=300, y=20, width=50, height=25)
output_lbl = Label(text="Answer = ")
output_lbl.place(x=50, y=50, width=100, height=25)
output_txt = Message(text=0)
output_txt.place(x=150, y=50, width=100, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"
clear_btn = Button(text="Clear", command=reset)
clear_btn.place(x=300, y=50, width=50, height=25)
window.mainloop()



from tkinter import *
def add_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()
def clear_list():
    name_list.delete(0, END)
    name_box.focus()
window = Tk()
window.title("Names list")
window.geometry("400x200")
label1 = Label(text = "Enter a name: ")
label1.place(x = 20, y = 20, width = 100, height = 25)
name_box = Entry(text = 0)
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box.focus()
button1 = Button(text = "Add to list", command = add_name)
button1.place(x = 250, y = 20, width = 100, height = 25)
name_list = Listbox()
name_list.place(x = 120, y = 50, width = 100, height = 100)
button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)
window.mainloop()
def convert2():
    km = textbox1.get()
    km = int(km)
    message = km * 0.6214
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, " miles")
window = Tk()
window.title("Distance")
window.geometry("260x200")
label1 = Label(text = "Enter the value you want to convert: ")
label1.place(x = 30, y = 20)
textbox1 = Entry(text = "")
textbox1.place(x = 30, y = 50, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()
convert1 = Button(text = "Convert miles to km", command = convert1)
convert1.place(x = 30, y = 80, width = 200, height = 25)
convert2 = Button(text = "Convert km to miles", command = convert2)
convert2.place(x = 30, y = 110, width = 200, height = 25)
textbox2 = Entry(text = "")
textbox2.place(x = 30, y = 140, width = 200, height = 25)
textbox2["justify"] = "center"
window.mainloop()


from tkinter import *
def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END, num)
        num_box.delete(0, END)
        num_box.focus()
    else:
        num_box.delete(0, END)
        num_box.focus()
def clear_list():
    num_list.delete(0, END)
    num_box.focus()
window = Tk()
window.title("Number list")
window.geometry("400x200")
label1 = Label(text = "Enter a number: ")
label1.place(x = 20, y = 20, width = 100, height = 25)
num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()
button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)
num_list = Listbox()
num_list.place(x = 120, y = 50, width = 100, height = 100)
button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)
window.mainloop()

from tkinter import *
import csv
def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END, num)
        num_box.delete(0, END)
        num_box.focus()
    else:
        num_box.delete(0, END)
        num_box.focus()
def clear_list():
    num_list.delete(0, END)
    num_box.focus()
def save_list():
    file = open("numbers.csv", "w")
    tmp_list =num_list.get(0, END)
    item = 0
    for x in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item + 1
    file.close()
window = Tk()
window.title("Number list")
window.geometry("400x200")
label1 = Label(text = "Enter a number: ")
label1.place(x = 20, y = 20, width = 100, height = 25)
num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()
button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)
num_list = Listbox()
num_list.place(x = 120, y = 50, width = 100, height = 100)
button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)
button3 = Button(text = "Save list", command = save_list)
button3.place(x = 250, y = 80, width = 100, height = 25)
window.mainloop()


from tkinter import *
import csv
def create_new():
    file = open("ages.csv", "w")
    file.close()
def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + ", " + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()
window = Tk()
window.title("People list")
window.geometry("400x100")
label1 = Label(text = "Enter a name: ")
label1.place(x = 20, y = 20, width = 100, height = 25)
name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box["justify"] = "left"
name_box.focus()
label2 = Label(text = "Enter their age: ")
label2.place(x = 20, y = 50, width = 100, height = 25)
age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"
button1 = Button(text = "Create new file", command = create_new)
button1.place(x = 250, y = 20, width = 100, height = 25)
button2 = Button(text = "Add to file", command = save_list)
button2.place(x = 250, y = 50, width = 100, height = 25)
window.mainloop()


from tkinter import *
import csv
def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + ", " + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()
def read_list():
    name_list.delete(0, END)
    file = list(csv.reader(open("ages.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END, data)
        x = x + 1
window = Tk()
window.title("People list")
window.geometry("400x200")
label1 = Label(text = "Enter a name: ")
label1.place(x = 20, y = 20, width = 100, height = 25)
name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box["justify"]="left"
name_box.focus()
label2 = Label(text = "Enter their age: ")
label2.place(x = 20, y = 50, width = 100, height = 25)
age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"]="left"
button1 = Button(text = "Add to file", command = save_new)
button1.place(x = 250, y = 20, width = 100, height = 25)
button2 = Button(text = "Read list", command = read_list)
button2.place(x = 250, y = 50, width = 100, height = 25)
label3 = Label(text = "Saved names: ")
label3.place(x = 20, y = 80, width = 100, height = 25)
name_list = Listbox()
name_list.place(x = 120, y = 80, width = 230, height = 100)
window.mainloop()

from tkinter import *
def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["text"] = message
window = Tk()
window.title("Names")
window.geometry("450x350")
window.wm_iconbitmap("stripes.ico")
window.configure(background = "black")
logo = PhotoImage(file = "Mylogo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 100, y = 20, width = 200, height = 150)
label1 = Label(text = "Enter your name: ")
label1.place(x = 30, y = 200)
label1["bg"] = "black"
label1["fg"] = "white"
textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 200, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()
button1 = Button(text = "Press me", command = click)
button1.place(x = 30, y = 250, width = 120, height = 25)
button1["bg"] = "yellow"
textbox2 = Message(text = "")
textbox2.place(x = 150, y = 250, width = 200, height = 25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"
window.mainloop()


from tkinter import *
import random
def checkans():
    theirans = ansbox.get()
    theirans = int(theirans)
    num1 = num1box["text"]
    num1 = int(num1)
    num2 = num2box["text"]
    num2 = int(num2)
    ans = num1 + num2
    if theirans == ans:
        img = PhotoImage(file = "correct.gif")
        imgbx.image = img
    else:
        img = PhotoImage(file = "wrong.gif")
        imgbx.image = img
    imgbx["image"] = img
    imgbx.update()
def nextquestion():
    ansbox.delete(0, END)
    num1 = random.randing(10, 50)
    num1box["text"] = num1
    num2 = random.randing(10, 50)
    num2box["text"] = num2
    img = PhotoImage(file = "")
    imgbx.image = img
    imgbx["image"] = img
    imgbx.update()
window = Tk()
window.title("Addition")
window.geometry("250x300")
num1box = Label(text = "0")
num1box.place(x = 50, y = 30, width = 25, height = 25)
addsymbl = Message(text = "+")
addsymbl.place(x = 75, y = 30, width = 25, height = 25)
num2box = Label(text = "0")
num2box.place(x = 100, y = 30, width = 25, height = 25)
eqlsymbl = Message(text = "=")
eqlsymbl.place(x = 125, y = 30, width = 25, height = 25)
ansbox = Entry(text = "")
ansbox.place(x = 150, y = 30, width = 25, height = 25)
ansbox["justify"] = "center"
ansbox.focus()
checkbtn = Button(text = "Check", command = checkans)
checkbtn.place(x = 50, y = 60, width = 75, height = 25)
nextbtn = Button(text = "Next", command = nextquestion)
nextbtn.place(x = 130, y = 60, width = 75, height = 25)
img = PhotoImage(file = "")
imgbx = Label(image = img)
imgbx.image = img
imgbox.place(x = 25, y = 100, width = 200, height = 150)
nextquestion()
window.mainloop()


from tkinter import *
def clicked():
    sel = selectcolour.get()
    window.configure(background = sel)
window = Tk()
window.title("background")
window.geometry("200x200")
selectcolour = StringVar(window)
selectcolour.set("Grey")
colourlist = OptionMenu(window, selectcolour, "Grey", "Red", "Blue", "Green", "Yellow")
colourlist.place(x = 50, y = 30)
clickme = Button(text = "Click Me", command = clicked)
clickme.place(x = 50, y = 150, width = 60, height = 30)
mainloop()


from tkinter import *
def add_to_list():
    name = namebox.get()
    namebox.delete(0, END)
    genderselection = gender.get()
    gender.set("M/F")
    newdata = name + ", " + genderselection + "\n"
    name_list.insert(END, newdata)
    namebox.focus()
window = Tk()
window.title("People list")
window.geometry("400x400")
namelbl = Label(text = "Enter their name: ")
namelbl.place(x = 50, y = 50, width = 100, height = 25)
namebox = Entry(text = "")
namebox.place(x = 150, y = 50, width = 150, height = 25)
namebox.focus()
genderlbl = Label(text = "Select Gender")
genderlbl.place(x = 50, y = 100, width = 100, height = 25)
gender = StringVar(window)
gender.set("M/F")
gendermenu = OptionMenu(window, gender, "M", "F")
gendermenu.place(x = 150, y = 100)
name_list = Listbox()
name_list.place(x = 150, y = 150, width = 150, height = 100)
addbtn = Button(text = "Add to List", command = add_to_list)
addbtn.place(x = 50, y = 300, width = 100, height = 25)
window.mainloop()


from tkinter import *
def add_to_list():
    name = namebox.get()
    namebox.delete(0, END)
    genderselection = gender.get()
    gender.set("M/F")
    newdata = name + ", " + genderselection + "\n"
    name_list.insert(END, newdata)
    namebox.focus()
    file = open("names.txt", "a")
    file.write(newdata)
    file.close()
def print_list():
    file = open("names.txt", "r")
    print(file.read())
window = Tk()
window.title("People list")
window.geometry("400x400")
namelbl = Label(text = "Enter their name:")
namelbl.place(x = 50, y = 50, width = 100, height = 25)
namebox = Entry(text = "")
namebox.place(x = 150, y = 50, width = 150, height = 25)
namebox.focus()
genderlbl = Label(text = "Select Gender")
genderlbl.place(x = 50, y = 100, width = 100, height = 25)
gender = StringVar(window)
gender.set("M/F")
gendermenu = OptionMenu(window, gender, "M", "F")
gendermenu.place(x = 150, y = 100)
name_list = Listbox()
name_list.place(x = 150, y = 150, width = 150, height = 100)
addbtn = Button(text = "Add to List", command = add_to_list)
addbtn.place(x = 50, y = 300, width = 100, height = 25)
printlst = Button(text = "Print List", command = print_list)
printlst.place(x = 175, y = 300, width = 100, height = 25)
window.mainloop()

from tkinter import *


def clicked():
    num = selection.get()
    artref = num + ".gif"
    photo = PhotoImage(file=artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()


window = Tk()
window.title("Art")
window.geometry("400x350")
art = PhotoImage(file="1.gif")
photobox = Label(window, image=art)
photobox.image = art
photobox.place(x=100, y=20, width=200, height=150)
label = Label(text="Select Art Number: ")
label.place(x=50, y=200, width=100, height=25)
selection = Entry(text="")
selection.place(x=200, y=200, width=100, height=25)
selection.focus()
button = Button(text="See Art", command=clicked)
button.place(x=150, y=250, width=100, height=25)
window.mainloop()


