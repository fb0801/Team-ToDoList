'''
student name: Farhan Bhatti
Student id: 3712356
student email: bhattif3@lsbu.ac.uk

student name: Raima Butt
student id:
student email:
'''
#imports the tkinter and sys libary
from tkinter import *
from tkinter import messagebox
import sys

# a dictoniray of months and their num of days
months = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May': 31, 'Jun':30,
          'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec': 31}
#list to store the task data
name = []
start_date= []
due_date = []
priority = []
status = []

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master) # a frame to contain everything in
        self.grid() # to say we are using grids
        self.screen() # to call the screen method

    def screen(self):
        self.master.title("Todo list")
        self.tlbl=Label(self, text = "Welcome to the LSBU To Do List!")
        self.tlbl.grid(row = 0, column = 5)# a label for the app
        Label(self, text="").grid(row = 1, column = 5)#a blank label  
        
        username_input = StringVar()#taking the user input as a string
        password_input = StringVar()#taking the user input as a string
        self.uselbl =Label(self, text = "Username:")
        self.uselbl.grid(row = 3, column = 3)# username label
        self.username_entry = Entry(self, textvariable=username_input)#entry box to take input
        self.username_entry.grid(row = 3, column = 6)#to place the the entry box on the window

        Label(self, text="").grid(row = 4, column = 5)# a blank label
        self.passlbl =Label(self, text = "Password:")
        self.passlbl.grid(row = 5, column = 3)# password label
        self.password_entry = Entry(self, textvariable = password_input, show='*')#password label which changes text to 8
        self.password_entry.bind("<Return>", self.login) # a event to press the enter key to access the home_page and check login details
        self.password_entry.grid(row = 5, column = 6)# to place the label on the window
        #Label(root, text="").pack()# a blank label
        self.loginbtn=Button(self, text="Login", width=10, height=1, command = self.login)
        self.loginbtn.grid(row = 8, column =7)# a button for the user to click on to login
        #Label(root, text="").g()# a blank label
        self.close=Button(self, text ="Quit", width = 10, height = 1, command =root.destroy)
        self.close.grid(row = 8, column =8)# a quit button to exit the application
        self.help_btn = Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = Application.helpbtn)
        self.help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)

    def login(self, event=None):
        if self.username_entry.get() == 'farhan' and self.password_entry.get() == 'chelsea':#checks the entered login details by the user
            #self.home_page()
            Application.hide_me(self)
            #Application.Home_page(self) #opens the home_page method from the Task class
        elif self.username_entry.get() == 'raima' and self.password_entry.get() == 'software':#checks the entered login details by the user
            #self.home_page()
            Application.hide_me(self)
            #Application.Home_page(self)#opens the home_page method from the Task class
        elif self.username_entry.get() == 'guest' or self.password_entry.get() == 'guest':#checks the entered login details by the user
            #self.home_page()
            #Application.Home_page(self) #opens the home_page method from the Task clsss
            Application.hide_me(self)
        else:
            messagebox.showerror("Invalid", "Incorrect username or password") # if a task is not given a name a error messagebox appears
    def hide_me(self):
        ''' A method to hide the widgets on the login screen'''
        self.username_entry.grid_forget()
        self.password_entry.grid_forget()
        self.tlbl.grid_forget()
        self.uselbl.grid_forget()
        self.close.grid_forget()
        self.passlbl.grid_forget()
        self.help_btn.grid_forget()
        self.loginbtn.grid_forget()
        Application.Home_page(self)
    def helpbtn():   
        messagebox.showinfo("Help", "Enter your login details to access the To Do List") # if the user clicks on help this messagebox will appear 


    def Home_page(self):
        #root = Tk()
        #root.title("Todo list") # title of the application
        root.geometry("900x400") # size of the application
        #self.grid()
        titlelbl=Label(self, text = 'Welcome to your To-do-list', font='Times 30  bold').grid(row=0, column=5)#pack(),place(x = 25, y = 30)
        Label(self, text = "Name").grid(row = 6, column = 4)#pack()

        self.name = Entry(self, textvariable = name_input)
        self.name.grid(row = 7, column = 4)#pack()

        Label(self, text = "Start date").grid(row = 6, column = 5)#pack()
        self.start_date = Entry(self, textvariable = start_date_input)
        self.start_date.grid(row = 7, column = 5)#pack()

        Label(self, text = "Due date").grid(row = 6, column = 6)#pack()
        self.due_date = Entry(self, textvariable = due_date_input).grid(row = 7, column = 6)#pack()

        Label(self, text = "Priority").grid(row = 6, column = 7)#pack()
        self.priority = Entry(self, textvariable = pri_input)
        self.priority.grid(row = 7, column = 7)#pack()

        Label(self, text = "Status").grid(row = 6, column = 8)#pack()
        self.status = Entry(self, textvariable = status_input)
        self.status.grid(row = 7, column = 8)#pack()

        add_btn = Button(self, text = 'Add', width = 10, height = 3, command = self.add_task)
        add_btn.grid(row = 9, column= 7)#pack()#place(x = 15, y = 50)

        self.listbox = Listbox(self,font=('', 12), width = 60, height = 10)
        self.listbox.grid(row = 3, column = 5)#pack()
        self.listbox.insert(1, 'Name          Start date          Due Date       Priority        Status')

        del_btn=Button(self, text = 'Delete but sel', width = 10, height = 3,command = self.delete_task).grid(row = 9, column = 8)#pack()
        delete_btn=Button(self, text = 'Delete', width = 10, height = 3, command =self.delete_item).grid(row= 9, column = 6)
        mod_btn =Button(self, text = 'Modify', width = 10, height = 3).grid(row = 9, column = 9)#pack()
        Button(root, text = 'Exit', width = 10, height = 3, command = root.destroy).grid(row = 12, column = 8)#pack()
        btn2 = Button(self, text = '?', font = 'Times 20 ',width = 1, height = 1, command = self.helpbtn_2).grid(row = 12, column = 9)
        Button(self, text = 'Clear',width = 10, height = 3, command = self.clear_all).grid(row =9, column =10)

    def helpbtn_2(self):
        messagebox.showinfo("Help", 'Welcome to the To-Do-List\n\nPress add to add your task along with the details needed\nPress delete to remove your task\nPress modify to change your tasks details')# a info messagebox which explains how to use the app

    '''def clear_all():
        self.listbox.delete(0,END)'''

    def delete_item(self):
        '''Gets the current location of the cursor and delete item'''
        current_sel = self.listbox.curselection()
        self.listbox.delete(current_sel)
        
    def modify(self):
        '''Modify the item to be something else'''
        pass

    def delete_task(self):
        '''Delete everything but selected item'''
        current_sel = self.listbox.curselection()
        self.listbox.delete(1, current_sel[0] -2)#2,0
        self.listbox.delete(2, END)

    def add_task(self):
        '''Add a task to the listbox'''
        task = name_input.get()
        start_dte = start_date_input.get()
        due_dte = due_date_input.get()
        pri = pri_input.get()
        stat = status_input.get()
        # end
        if task !="":
            '''self.listbox.insert(1, task)
            self.listbox.insert(1, start_dte)
            self.listbox.insert(1, due_dte)
            self.listbox.insert(1, pri)
            self.listbox.insert(1, stat)'''
            test_string = task+"          "+start_dte+"          "+due_dte+"          "+pri+"          "+stat
            self.listbox.insert(1,test_string)#adds the data to the listbox
            name.append(task)#add to list
            start_date.append(start_dte) #add to list
            due_date.append(due_dte)#add to list
            priority.append(pri)#add to list
            status.append(stat)#add to list
        else:
            messagebox.showerror("Error", 'Please enter a task name')# a info messagebox which explains how to use the app


    def clear_all(self):
        '''Remove everything in the listbox'''
        self.listbox.delete(1,END)#delete everything in the listbox
        
root = Tk()

name_input = StringVar()
start_date_input = StringVar()
due_date_input = StringVar()
pri_input = StringVar()
status_input = StringVar()

app = Application(root)
root.mainloop()
