from tkinter import *
from PIL import Image, ImageTk
from datetime import date

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("AGE CALCULATOR")

# Open the image using PIL
image = Image.open("age.png")

# Resize the image
image = image.resize((200, 200))

# Convert the image to Tkinter-compatible format
photo = ImageTk.PhotoImage(image)

my_image = Label(image=photo)
my_image.pack()

def calculate_age():
    today=date.today()
    birthdate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    Label(text=f"{nameValue.get()} your age is {age} ", font=30).place(x=300,y=500)



Label(text="Name", font=20).place(x=200, y=250)
Label(text="Year", font=20).place(x=200, y=300)
Label(text="Month", font=20).place(x=200, y=350)
Label(text="Day", font=20).place(x=200, y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=10,font=20,bd=3)
nameEntry.place(x=300,y=250)
yearEntry=Entry(root,textvariable=yearValue,width=10,font=20,bd=3)
yearEntry.place(x=300,y=300)
monthEntry=Entry(root,textvariable=monthValue,width=10,font=20,bd=3)
monthEntry.place(x=300,y=350)
dayEntry=Entry(root,textvariable=dayValue,width=10,font=20,bd=3)
dayEntry.place(x=300,y=400)

b1=Button(text="CALCULATE AGE",font=20,bg="black",fg="white",width=15,height=2,command=calculate_age).place(x=300,y=450)
root.configure(bg="grey")
root.mainloop()

