#coding: utf-8
#Ewan GRIGNOUX LEVERT
#July 2020
import sys
import csv
from tkinter import *

#Variables
backgroung_color = '#2E2E2E'

#Functions
def ReadCSVFile(File):
    table = []
    with open (File, newline = '', encoding = 'utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter = ',')
        for element in lecteur:
            table.append(element)
    return table

Tasks = ReadCSVFile('Tasks.csv')
row_count = lambda : sum(1 for row in Tasks)
num = row_count()-1


def NewTaskDisplay():

    def SaveTask():
        global num
        name = str(Name.get())
        description = str(Description.get())
        num +=1
        
        new_line = [num, name, description, False]
        
        with open ('Tasks.csv', 'a+', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(new_line)

    window = Toplevel()
    window.title('Add a new task')
    window.geometry('720x480+300+300')
    window.configure(bg = backgroung_color)

    name_task = StringVar()
    name_task.set('Name of the new task')
    description_task = StringVar()
    description_task.set('Description of the new task')

    Name = Entry(window, textvariable = name_task, bg = backgroung_color, fg = 'white', width = 30, font = (20))
    Name.pack(padx=5, pady=5)
    Description = Entry(window, textvariable = description_task, bg = backgroung_color, fg = 'white', width = 30, font = (30))
    Description.pack(padx=5, pady=5)
    Save = Button(window, text='Save Task', bg = backgroung_color, fg='white', font = (20), command = SaveTask)
    Save.pack(padx=5, pady=5)

#Root
root = Tk()
root.title('To Do List')
root.geometry('1080x720+200+75')
root.configure(bg = backgroung_color)

#Frames
frame1 = Frame(root, bg = backgroung_color, width=1080, height=60)
frame1.pack(side=TOP, fill=X)

#Element of display
New = Button(frame1, text='New Task', bg = backgroung_color, fg='white', command = NewTaskDisplay, font = (20))
New.pack(side=RIGHT)

root.mainloop()
sys.exit()