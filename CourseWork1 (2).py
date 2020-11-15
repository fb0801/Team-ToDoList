'''Raima Butt
3800348
rbutt@lsbu.ac.uk'''

#-----------------Menu Function---------------
'''Displays Menu'''

def menu ():
    print("\
1- Create Database\n\
2- Add a new employee\n\
3- Remove an existing employee\n\
4- Edit details of existing employee\n\
5- Search and display details of employee\n\
6- Exit\n")
    
#-------------------Dictionary Function------------
'''Stores all the employees details in a dictionary'''

def diction():
    dict1={"ID":input("Please enter ID\n"), #Values for all of the keys are taken from input
          "First Name":input("Please enter first name\n"),
          "Last Name":input("Please enter last name\n"),
          "Department":input("Please enter department\n"),
          "Designation":input("Please enter designation\n"),
          "Join Date":input("Please enter date joined dd.mm.yy\n"),
          "Status":input("Please enter status\n")}
    return dict1 

#--------------File List Function-----------
'''Reads data from file and stores in a list'''

def fileLine():
    lines=[] #Declaring an empty list to store the line in the file
    with open ('cw1.csv','rt')as f:
        for line in f:
            lines.append(line) #Appends each line of the file into the list
    (lines[1:])   

    for d,line in enumerate(lines): #Gives each line a number 
        print(d,line,end='')

#------------------Creating Database Function---------------
'''Creates the database by adding columns to the file'''

def dataBase():
    titleID='ID' #Column headings 1
    titlefName='First Name' #Column headings 2
    titlelName='Last Name' #Column headings 3
    titleDepartment='Department' #Column headings 4
    titleDesignation='Designation' #Column headings 5
    titleJoinDate='Join Date' #Column headings 6
    titleStatus='Status' #Column headings 7

    with open('cw1.csv','w') as f:
        f.write('%s,%s,%s,%s,%s,%s,%s,\n'      
          %(titleID,titlefName,titlelName,titleDepartment,   
            titleDesignation,titleJoinDate,titleStatus))   #Writes title headings to file
        
#------------------Instructions----------------------
print('Hello and Welcome.\nThis porgram has been deisgned to keep employees in an organised database.\n\n\
Before you get started please read the information below carefully.\n\
If it is your first time using this program, please choose the option to first create a database (1)\n\
This will create the database with its correct headings.\n\
If this is not done and the option is selected to add an employee, the program will still add the employee \
but there will be no headings or database.\n\
Once you create a new database, you do not need to create it again the next time the program is opened.\n\
If this is done, the present database and all its information will be deleted and replaced with a new empty \
database.\n\n')

#-------------------Menu Function call---------------
x=('Y')
while x=='Y' : # As long as x=Y, the menu function will run
    menu()
#-----------------Option 1---------------------
    
    option=input("Please choose an option from the menu\n")

    if option=='1':
        dataBase() #Function call to create database
        x=input('Congratulations your database as successfully been created.\
                                Do you wish to continue? (Y/N)\n')
        #If user inputs Y, menu function will run, else program will end


#------------------Option 2--------------------------
    elif option=='2':
            dictemp=diction() #Function call to add employee details to dictionary
                
            with open('cw1.csv','a',encoding = 'utf-8')as f:
                ID='NAME'
                First_Name=(dictemp['First Name'])
                Last_Name=(dictemp['Last Name'])
                Department=(dictemp['Department'])
                Designation=(dictemp['Designation'])
                Join_Date=(dictemp['Join Date'])
                Status=(dictemp['Status'])

                f.write('%s,%s,%s,%s,%s,%s,%s,\n'\
                        %(ID,First_Name,Last_Name,Department,\
                          Designation,Join_Date,Status))
                
                 #Creates a dictionary and adds the employee details to the file                 
                
            x=input('Press Y to continue?\n')
            
#----------------Option 3---------------------------
    elif option=='3':
        fileLine() #Function call to store data from file into a list

        dell=[]
        with open ('cw1.csv','rt')as f:
            for line in f:
                print (line)
                dell.append(line) #Appends data from the file into the empty list
        (dell[1:])




#------------------------------------------------
    else:
        print('Error option not found!\n')
        x=input('Press Y to continue?\n')
