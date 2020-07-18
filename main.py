#coding: utf-8
#Ewan GRIGNOUX LEVERT
#July 2020
import sys
import csv
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import*

#Variables
background_color = '#2E2E2E'
font_color = 'white'
green = '#298A08'
red ='#DF0101'
grey = '#848484'
list_of_tasks = []
list_of_folders = []
list_of_folders_button = []

#Functions
def ReadCSVFile(File):
    table = []
    with open (File, newline = '', encoding = 'utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter = ',')
        for element in lecteur:
            table.append(element)
    return table

Tasks = ReadCSVFile('Tasks.csv')

def NewTaskDisplay():
    #This function create the display for save a new task
    global list_of_folders
    def SaveTask():
        name = str(Name.get())
        description = str(Description.get())
        folder = str(Folder.get())
        if folder == '':
            if askokcancel('Folder',"If you don't indicates folder, your task are automatically store in None"):
                folder = 'None'
                new_line = [name, description, folder]
                
                with open ('Tasks.csv', 'a+', newline='', encoding='utf-8') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(new_line)
                
                Refresh()
                window.destroy()
        else:
            new_line = [name, description, folder]
                
            with open ('Tasks.csv', 'a+', newline='', encoding='utf-8') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(new_line)
                
            Refresh()
            window.destroy()

    

    window = Toplevel()
    window.title('Add a new task')
    window.geometry('720x480+300+300')
    window.configure(bg = background_color)

    name_task = StringVar()
    name_task.set('Name of the new task')
    description_task = StringVar()
    description_task.set('Description of the new task')

    
    Tasks = ReadCSVFile('Tasks.csv')
    for i in range(len(Tasks)):
        if Tasks[i]['Folder'] not in list_of_folders:
            list_of_folders.append(Tasks[i]['Folder'])

    Name = Entry(window, textvariable = name_task, bg = background_color, fg=font_color, width = 30, font = (20))
    Name.pack(padx=5, pady=5)
    Description = Entry(window, textvariable = description_task, bg = background_color, fg=font_color, width = 30, font = (20))
    Description.pack(padx=5, pady=5)
    Folder = ttk.Combobox(window, values=list_of_folders, width=30)
    Folder.pack(padx=5, pady=5)
    Save = Button(window, text='Save Task', bg = green, fg=font_color, font = (20), command = SaveTask)
    Save.pack(padx=5, pady=5)

def ClickTask(i, liste):
    return lambda: ShowTask(i, liste)

def ShowTask(i, liste):
    #This function show the description of tasks ,in a new display, when we click on it.
    global list_of_tasks
    def Done():
        #This function delete the open task
        list_of_folders.remove(liste[i]['Folder'])
        
        with open(f'Tasks.csv', 'w', newline='', encoding = 'utf-8')as f:
            titres = ['Name', 'Description', 'Folder']
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
    infos.geometry('480x200+700+300')
    infos.configure(bg=background_color)
    description_label = Label(infos, text=liste[i]['Description'], fg=font_color, font=(20), bg=background_color, wraplength = 300)
    description_label.pack(padx=5, pady=5)
    done = Button(infos, text='Done', command=Done, fg=font_color, bg=red)
    done.pack(padx=5, pady=5, side = BOTTOM)

def Refresh():
    #This function, refresh the frame with buttons(tasks) in it.
    global list_of_folders, list_of_folders_button
    Tasks = ReadCSVFile('Tasks.csv')
    
    for i in range(len(Tasks)):
        if Tasks[i]['Folder'] not in list_of_folders:
            list_of_folders.append(Tasks[i]['Folder'])

    for btn in list_of_tasks:
        btn.forget()

    def ClickFolder(folder):
        return lambda: FrameTasks(folder)
    
    def FrameTasks(folder):
        #This function upgrade the frame2 with tasks in folder that the user has selected.
        j = -1
        for i in range(len(Tasks)):
            if Tasks[i]['Folder'] == folder:
                list_of_tasks.append(Button(frame2))
                j+=1
                list_of_tasks[j].configure(text=Tasks[i]['Name'], command = ClickTask(i, Tasks), bg = background_color, fg=font_color, font=(20))
                list_of_tasks[j].pack(fill=X, padx=5, pady=5)
    
    for button in list_of_folders_button:
        button.forget()

    for i in range (len(list_of_folders)):
        list_of_folders_button.append(Button(frame3))
        if list_of_folders[i] == 'None':
            list_of_folders_button[i].configure(text='None', command=ClickFolder('None'), bg=background_color, fg=font_color, font=(20))
        else:
            list_of_folders_button[i].configure(text=Tasks[i]['Folder'], command=ClickFolder(Tasks[i]['Folder']), bg=background_color, fg=font_color, font=(20))
        list_of_folders_button[i].pack(fill=X, padx=5, pady=5)

#Root, the principal display
root = Tk()
root.title('To Do List')
root.geometry('1280x750+300+75')

root.configure(bg = background_color)

#Element(s) of root
frame1 = Frame(root, bg = background_color, height=30)
frame1.pack(side=TOP, fill=X)

frame2 = LabelFrame(root, text='My Tasks', fg=font_color,font=(20), bg = background_color, width = 1100, height= 690)
frame2.pack(side=RIGHT, padx=5, pady=5)
frame2.pack_propagate(False)

frame3 = LabelFrame(root, text='My Folders', fg=font_color, font=(20), bg=background_color, width=170, height=690)
frame3.pack(side=LEFT, padx=5, pady=5)
frame3.pack_propagate(False)

New = Button(frame1, text='+ New Task', bg = green, fg=font_color, command = NewTaskDisplay, font = (20))
New.pack(side=LEFT)

Refresh()

root.mainloop()
sys.exit()