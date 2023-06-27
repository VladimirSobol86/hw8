
#Чтение всего справочника
def readData (filename):
    with open(filename) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

#Вывод всего справочника
def selectAllReadPhoneNumber ():
    phoneBook = readData(template)
    for i in phoneBook:
        print (i)

#Найти запись по id
def findID ():
    phoneBook = readData(template)
    flag = False
    phoneNumber = str(input("Enter personal ID:"))
    for i in phoneBook:
        if (phoneNumber == str(i[0])):
            print (i[0], i[1], i[2], i[3], i[4])
            flag = True
    return flag

#Перезаписать свежие данные в файл
def writeData (fileName, phoneBook):
    with open (fileName, 'w') as f:
        for i in phoneBook:
            f.write (','.join(i))
        print('Data added and saved')

#Добавить строку в файл
def addPerson ():
    phoneBook = readData(template)
    maxID = 0
    for i in phoneBook:
        if (maxID < int(i[0])):
            maxID = int(i[0])
    print ("Enter data:")
    number = str(len(phoneBook) + 1)
    surname = str(input("Enter surname:"))
    nameFirst = str(input("Enter first name:"))
    nameSecond = str(input("Enter second name:"))
    phoneNumber = str(input("Enter telephone number:"))
    n = ' \n'
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber, n])
    writeData(template, phoneBook)

#Редактирование записи
def editPerson ():
    phoneBook = readData(template)
    print ("Edit data:")
    editID = int(input("Enter ID to edit person:"))
    for i in phoneBook:
        if (editID == int(i[0])):
            print (i[0], i[1], i[2], i[3], i[4])
            newSurName = str(input("Enter new surname:"))
            newFirstName = str(input("Enter new first name:"))
            newSecondName = str(input("Enter new second name:"))
            newPhoneNumber = str(input("Enter new telephone number:"))
            n = ' \n'
            phoneBook[phoneBook.index(i)] = ([str(editID), newSurName, newFirstName, newSecondName, newPhoneNumber, str(n)])
            writeData(template, phoneBook)    

#Удаление строки
def deletePerson ():
    phoneBook = readData(template)
    print ("Delete data:")
    editID = int(input("Enter ID to delete person:"))
    for i in phoneBook:
        if (editID == int(i[0])):
            phoneBook.pop(phoneBook.index(i))
            writeData(template, phoneBook)   
            
#Тело программы
import os
template = ('..\урок8(семинар)\phonebook.txt')
os.system ('cls')
print('''Hello, user 
\n [1] -- press for SHOW ALL 
\n [2] -- press for SELECT 
\n [3] -- press for ADD
\n [4] -- press for EDIT
\n [5] -- press for DELETE''')

while True:
     enteredNum = int(input('Select the function you need: '))
     try:
         if (enteredNum == 1):
             selectAllReadPhoneNumber()
         elif (enteredNum == 2):
             findID()
         elif (enteredNum == 3):
             addPerson()
         elif (enteredNum == 4):
             editPerson()
         elif (enteredNum == 5):
             deletePerson()
         else: print("Your number out of range. Try again")
         break
     except:
         print("It's not a number")