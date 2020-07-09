#coding: utf-8
#Ewan GRIGNOUX LEVERT
#July 2020
import sys
import csv
from tkinter import *

#Variables
backgroung_color = '#2E2E2E'
list_of_tasks = []

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

def NewTaskDisplay():
    #This function create the display for save a new task
    def SaveTask():
        name = str(Name.get())
        description = str(Description.get())
        
        new_line = [name, description]
        
        with open ('Tasks.csv', 'a+', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(new_line)
        Refresh()
        window.destroy()


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
    Description = Entry(window, textvariable = description_task, bg = backgroung_color, fg = 'white', width = 30, font = (20))
    Description.pack(padx=5, pady=5)
    Save = Button(window, text='Save Task', bg = backgroung_color, fg='white', font = (20), command = SaveTask)
    Save.pack(padx=5, pady=5)

def ClickTask(i, liste):
    return lambda: ShowTask(i, liste)

def ShowTask(i, liste):
    #This function show the description of tasks ,in a new display, when we click on it.
    def Done():
        with open(f'Tasks.csv', 'w', newline='', encoding = 'utf-8')as f:
            titres = ['Name', 'Description']
            ecrivain = csv.DictWriter(f, fieldnames=titres)
            ecrivain.writeheader()
            for (index, compartiment) in enumerate(liste):
                if (index == i):
                    continue

                ecrivain.writerow(compartiment)
        Refresh()
        infos.destroy()
    infos = Toplevel()
    infos.title = liste[i]['Name']
    infos.geometry('720x480+300+300')
    infos.configure(bg=backgroung_color)
    description_label = Label(infos, text=liste[i]['Description'], fg='white', bg=backgroung_color, wraplength = 100)
    description_label.pack(padx=5, pady=5)
    done = Button(infos, text='Done', command=Done, fg='white', bg=backgroung_color)
    done.pack(padx=5, pady=5, side = BOTTOM)

def Refresh():
    #This function, refresh the frame with buttons(tasks) in it.
    Tasks_refresh = ReadCSVFile('Tasks.csv')
    for btn in list_of_tasks:
        btn.pack_forget()
    for i in range(len(Tasks_refresh)):
        list_of_tasks.append(Button(frame2))
        list_of_tasks[i].configure(text=Tasks_refresh[i]['Name'], command = ClickTask(i, Tasks_refresh), bg = backgroung_color, fg='white', font=(20))
        list_of_tasks[i].pack(fill=X, padx=5, pady=5)

#Root, the principal display
root = Tk()
root.title('To Do List')
root.geometry('1080x720+200+75')
root.configure(bg = backgroung_color)

#Element(s) of root
frame1 = Frame(root, bg = backgroung_color, height=30)
frame1.pack(side=TOP, fill=X)
frame2 = LabelFrame(root, text='My Tasks', fg = 'white',font=(20), bg = backgroung_color, width = 900, height= 690)
frame2.pack(anchor=SE, padx=5, pady=5, expand=YES)
frame2.pack_propagate(False)
New = Button(frame1, text='New Task', bg = backgroung_color, fg='white', command = NewTaskDisplay, font = (20))
New.pack(side=LEFT)

Refresh()

root.mainloop()
sys.exit()
