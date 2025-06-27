# student management system
print('_____________________________________________________________________')
print('\n       ****WELCOME TO STUDENT MANAGEMENT SYSTEM****')
sms=open('database.txt','a+')

def view_list():
    sms=open('database.txt','r')
    for i in sms:
        print(i)
    sms.close()

def add_data():
    sms=open('database.txt','a+')
    x=input('enter the name:')
    x=x+'\n'
    sms.write(x)
    print('name added sucessfully...')
    sms.close()

def remove_data():
    sms=open('database.txt','a+')
    name=input('enter the name to remove:')
    a=a+'\n'
    sms.seek(0)
    rn=sms.readlines()
    if name in rn:
        rn.remove(name)
        print('record deleted sucessfully...',name)
        s=( )
        s=( ).join([str(i)for i in rn])
        f1=open('database.txt','w')
        f1.write(s)
        f1.close()
    else:
        print('record not found...')
    sms.close()

def search_data():
    sms=open('database.txt','r')
    s=input('\nenter the name to search:')
    readfile=sms.read()
    if s in readfile:
        print('name found')
    else:
        print('record not found...')
    sms.close()

while True:
     print('_____________________________________________________________________')
     print('                                                    ')
     print('please choose any one options:\n')
     print('1. to view student list')
     print('2. to add new list')
     print('3. to remove the data')
     print('4. to search data')
     print('5. exit')
     ch=int(input('\nenter your choice:'))
     if ch==1:
         view_list()
     elif ch==2:
        add_data()
     elif ch==3:
        remove_data()
     elif ch==4:
        search_data()
     elif ch==5:
        exit()
     else:
        print('wrong input')
     g=input('do u continue this (y/n):')
     print('____________________________')

     if(g=='y'):
        continue
     elif(g=='n'):
        break
