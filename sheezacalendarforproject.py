from tkinter import*
from tkcalendar import*

screen = Tk()
screen.minsize(800,600)
screen.title("Sheeza python project")
screen.configure(background="brown")

def selectDate():
    myDate=myCal.get_date()
    selectedDate = Label(text = myDate)
    selectedDate.place(x = 425, y=350)

myCal = Calendar(screen , setmode='day', date_pattern='d/m/yy')
myCal.place(x=350, y=100)

openCal= Button(screen ,text="select Date", command = selectDate)
openCal.place(x = 425, y= 300)
