a='start'
todolist=[]
print(' This program will help you create your to-do list')

def show ():
    print ('Menu')
    print ('Option 1: Add items to list')
    print ('Option 2: Mark item as completed')
    print ('Option 3: View the list of to- do items')
    print ('Option 4: Exit ')

while a!='4':
    show()
    a=input('Enter the option:')
    if a=='1':
        item=input('What needs to be done')
        todolist.append(item)
        print('Added the ',item ,'to do list')
    elif a=='2':
        item=input('What have you completd')
        if item in todolist:
            todolist.remove(item)
            print(' Item marked as done')
        else:
            print('item does not exist :(. Choose another option.')
    elif a=='3':
        print('View the to do item list')
        print(todolist)
    elif a=='4':
        print('Glad you finished all tasks')
    else:
        print('Please enter 1 , 2, 3 or 4 as option')

