#String reversal

"""line1 = "Am good in python"
words = line1.split(" ")
final_line = ""

for i in range(len(words)):
    one_word = words[i]
    if i % 2 == 0:
        one_word = words[i][::-1]
    final_line = final_line + " " + one_word
    print(final_line)"""
########################################################################
#keyword 
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
#'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""import keyword
print(keyword.kwlist)"""
###########################################################################
#To get input

"""name = input("Enter your name : ")
print(type(name))"""    # by default the type will be string for the input function

"""a = int(input("Enter value A :"))
b = int(input("Enter value B:"))
c = a+b
print(c)"""   #type will be int now 

#float number as input

"""a = float(input("Enter Value A:"))
b = float(input("Enter Value B:"))
c = a+b
print(c)"""

# how to get multiple inputs in onle line

"""name_1 , name_2, name_3 = input("Enter 3 names :").split(",")
print("name 1" , name_1 )
print("name 2" , name_2 )
print("name 3" , name_3 )"""
###################################################################################
#multiline string
""""""
paragraph = """
fgjhsg kjshxjk ankn
bxsqbbhjxnj nxakkas
hsqjhjan xkalkxk nk"""

"""print(paragraph)
print(type(paragraph)) """          #string
#####################################################################
#list

"""nums = []
print(type(nums))     #list

nums = [23,43,12]
print(nums[2])"""                #12

######################################################################
#join()

"""curr = ["23","45","13"]
print("$ ".join(curr))  """   

#can use join in only string
#########################################################################

#get paragraph as input

"""my_para = []
print("enter para:")

while True:
    line = input()
    if line:
        my_para.append(line)
    else:
        break

print('\n'.join(my_para))"""

####################################################################

#type casting   int() , float(), str()----> constructors

"""a = 10.3
print(type(a))

b = int(a)

print(b,type(b))"""

################################################################

#String class

my_name = "Vaishali1 is a mobile Automation7 tester"

"""print(my_name.upper())  #VAISHALI1 IS A MOBILE AUTOMATION7 TESTER
print(my_name.lower())  #vaishali1 is a mobile automation7 tester
print(my_name.title())  #Vaishali1 Is A Mobile Automation7 Tester
print(my_name.capitalize()) #Vaishali1 is a mobile automation7 tester
print(my_name.find('i')) #2
print(my_name.find('i',3))  #7
print(my_name.endswith('er')) #true
print(my_name.replace('is' , 'are')) #Vaarehali1 are a mobile Automation7 tester
print(my_name.startswith('V')) #True
print(my_name.count('i')) #5
name = "saravanan"
print(name.isupper())  #false
print(name.islower())  #true
print(name.isalnum())  #true
print(name.isalpha())   #true
print(name.isnumeric()) """ #false


"""s = "he\nis\ngood"
print(s)    
#he
#is
#good
print(s.splitlines())  #["he","is","good"]
print(s.splitlines(True)) #[he\n,is\n,good]"""


"""s = "he, is, good"
print(s.split(",")) """  #['he', ' is', ' good']

"""s = "  Vaishu  "
print(len(s.strip()))    #6
print(len(s.lstrip()))     #left side space will be removed
print(len(s.rstrip())) """   #right side space will be removed

"""date = "08-06-2023"
print(date.partition("-"))"""    #('08', '-', '06-2023')


##########################################################################################

#STRING MANIPULATION

#slicing

"""topic = "SLICING"
print(topic[0:2])     #SL
print(topic[:3])     #SLI
print(topic[1:])   #LICING
print(topic[-1])  #G
print(topic[0:-1])  #SLICIN
print(topic[:-1]) #SLICIN
print(topic[-2:-1]) #N
print(topic[::-1]) """# GNICILS  - String reversal

##########################################################################################

#ARITHMETIC OPERATORS

"""a=25
b = 10

print(a+b)    #35
print(a-b)  #15
print(a*b)   #250
print(a/b)  #2.5
print(a%b)  #5
print(a//b) #2
print(2**3) #8"""


#ARITHMETIC ASSINGNMENT OPEARATORS

#    == , += , -= ,*= , /= , **= =// .%=

#comparison or relational operator

#   ==,!= , <= ,>= , >,<

#logical operators

# and or not

#Bitwise operators


#######################################################################333
#ifnelse statement


"""name = input("Enter your name : ")
age = int(input("Enter your age"))
if age>= 18 :
    print( name, "of age " , age , " is eligible to vote" )
else:
    print( name, "of age " , age , " is not eligible to vote" )"""

#elif statement

"""days = int(input("Enter the number of days late : "))
if(days == 0):
    print("Good No fine")
elif(days >0 and days<=5):
    print("fine amount: ", days*0.5)
elif(days >5 and days<=10):
    print("fine amount: " , days*1)
elif(days >10 and days <=20):
    print("Fine amount: ", days*2)
elif(days>20 and days <=30):
    print("fine amount: ",days*3)
elif(days > 30):
    print("Membership cancel")"""

#Nested if

"""mark1 = int(input("Enter Mark 1: "))
mark2 = int(input("Enter Mark 2: "))
mark3 = int(input("Enter Mark 3: "))

total = mark1+mark2+mark3
print("Total Marks : ", total)
average = total/3
print("Average : ",average)

if mark1>35 and mark2>35 and mark3>35:
    print("Result : Pass")
    if(average > 90 and average <=100):
        print("Grade : A")
    elif(average >80 and average <=90):
        print("Grade : B")
    elif(average >70 and average <=80):
        print("Grade : C")
    elif(average < 70):
        print("Grade : D")
else:
    print("Result : Fail")"""



#######################################################################################

#looping statement


#WHILE
#print odd numbers from 1 to 20

"""n = 20
i = 1
while i <= 20:
    print(i)
    i+=2"""


#continue statemet - will go to next loop
"""i=1
while i<=19:                      
    i+=1
    if(i%2==0):
        continue
    print(i)"""


#break - will break the loop
"""i=1
while i<=20:
    if(i == 7):
        break
    print(i)
    i+=1"""


#For loop

"""for i in range(0,21 , 2):      #n-1    # 0 to 20 , 2 increment
    print(i)"""


"""*
   **
   ***
   ****
   *****
   *****
   ****
   ***
   **
   *"""


"""for i in range (6):
    for j in range(i):
        print("*" , end = "")
    print("")

for i in range(5,0,-1):
    for j in range(i):
        print("*" , end = "")
    print("")"""


# while else for else
"""i =1
while i<=20:                        # else will be executed once the loop is totally completed,
    print(i)                                    #incase if th
    i+=1                               #incase if the loop breaks in mid m else will not get executed
else:
    print("loop completed")


for i in range(1,20):
    print(i)
else:
    print("loop done")"""



##########################################################################33
#List  - sequence , mutable

"""a = [1,2,3,4,5]
print(type(a))
print(a[-1])    # 5 (reverse)
print(a[0:3])                  # slicing
print(a[2:])
print(a[:4])"""


"""b = [ 2, False , "Vaishu" , 3.6 , ['w','r','y','v']]  
print(b)                             #nested list
print(type(b))
print(type(b[0]))   #int
print(type(b[1]))  #bool
print((b[4][1]))   #r"""

#functions in list

"""r = [ 23, 54, 87, 4, 21 , 54]
print(r)
#r.clear()
print(r)
g = r.copy()
print(g)
print(r.count(54))
print(len(r))
print(max(r))
print(min(r))
print(r.index(4))
r.pop(2)    # remove by index
print(r)
r.remove(21)     #remove by value
print(r)
r.append(61)   #add value
print(r)"""


"""names = [ "ram","sam","madhu"]
name1 = ['anu' , 'sita']
names.extend(name1)     # adds one list to another list
print(names)

names.insert(0,"Vaishali")
print(names)"""

##list constructor

"""print(list(range(5)))   #[0, 1, 2, 3, 4]
print(list("Vaishali"))  #['V', 'a', 'i', 's', 'h', 'a', 'l', 'i']

a = [23,5,67,0]      
a.sort()   
print(a)               #[0, 5, 23, 67]
a.sort(reverse = True)
print(a)   
e = ['ram' , 'sita','yu']            #[67, 23, 5, 0]
e.sort(key=len)     #['yu', 'ram', 'sita']
print(e)"""


#####################################################################
#TUPLES  - immutable , surrounded by round brackets

"""a = (12,14,65)
print(a[0])    #12
print(type(a))   #tuple"""

#cannot change the values in tuple only by changing to list , we can modify

"""b = ('ram' , 'sita')
print(type(b))
c = list(b)
c.append('rani')
print(c)
print(type(c))
d = tuple(c)
print(type(d))"""

"""b = ('ram' , 'sita')
print(len(b))

for a in b:
    print(a)

if "ram" in b:
    print("Ram found")

a =(1)
print(type(a)) # int
a = (1,)
print(type(a))  #tuple

#tuple  can only be deleted permanently
del a

print(a)  #exception throws"""

#tuple concatenation

"""a = (1,2,3,4)
b = (5,6,7,8)
c = a+b
print(c)   #(1, 2, 3, 4, 5, 6, 7, 8)
print(c.count(5))   #1"""

#nested tuple
"""a = (1,2,3,4)
b = (5,6,7,8)

c = (a,b)
print(c)      #((1, 2, 3, 4), (5, 6, 7, 8))
print(c[0])   #(1, 2, 3, 4)
print(c[1])   #(5, 6, 7, 8)
print(c[0][1])  #2"""

#name = ('vaishali',)*10
#print(name) #('vaishali', 'vaishali', 'vaishali', 'vaishali', 'vaishali', 'vaishali', 'vaishali', 'vaishali', 'vaishali', 'vaishali')

"""a = (1,2,4,8)
print(min(a))  #1
print(max(a))  #8"""

##########################################################################################

#Set

#unordered and unindexed


a = {'Ram','Sam','Ravi'}
print(type(a))
""""
for name in a:
    print(name)

a.add("Sara")
print(a)    #{'Ravi', 'Ram', 'Sara', 'Sam'}
b = {'Mani','Ramesh'}
a.update(b)
print(a)  #{'Ramesh', 'Ram', 'Ravi', 'Sara', 'Sam', 'Mani'}

a.remove('Mani')
print(a) #{'Sara', 'Ram', 'Ravi', 'Ramesh', 'Sam'}

#not sure whether data is present or not , but to be removed use discard

a.discard("Mani")  #if we use remove and the value not there , it will throw exception
print(a)  #{'Sam', 'Ramesh', 'Sara', 'Ravi', 'Ram'}


a.pop()
print(a)   #{'Ram', 'Sam'}  last value in set will be removed, but it can be any as its keep on shuffling

a.clear()
print(a)  #set()

del a 
print(a)
"""

#SET will not allow duplicates
""""
names = {"ram","sam","rani","mani","ram"}
print(names) #{'sam', 'rani', 'mani', 'ram'}

a= {1,3,5,7}
b={'f','g','v'}
c=a.union(b)
print(c)   #{'f', 1, 3, 5, 7, 'g', 'v'}

a.update(b)   #will store in same var a
print(a) #{1, 'g', 3, 'f', 5, 7, 'v'}
"""
##########intersection
""""
a={1,2,3,4,5}
b = {5,6,7,8,9}

c=a.intersection(b)
print(c)   #{5}

a.intersection_update(b)
print(a)  #{5}
"""

#################symmetric difference
"""
c = a.symmetric_difference(b)
print(c) #{1, 2, 3, 4, 6, 7, 8, 9}
a.symmetric_difference_update(b)
print(a) #{1, 2, 3, 4, 6, 7, 8, 9}
"""

#a={1,2,3,4,5}
#b = {5,6,7,8,9}

#c = a.isdisjoint(b)
#print(c) #False            its a joint as common 5 is there
""""
a={5,6,7}
b = {5,6,7,8,9}

c= a.issubset(b)
print(c)   #True
d = b.issuperset(a)
print(d)     #True
"""

##############################Dictionary-key value pair
"""
data={
    "name" :"Ram",
    "age" : "45",
    "isemployed" :True
}

#keys should be duplicated

print(data)  #{'name': 'Ram', 'age': '45', 'isemployed': True}
print(type(data))   #<class 'dict'>

print(data["name"])  #Ram
print(data.get("age"))  #45
print(data.keys()) #dict_keys(['name', 'age', 'isemployed'])
print(data.values()) #dict_values(['Ram', '45', True])

print(data.items()) #dict_items([('name', 'Ram'), ('age', '45'), ('isemployed', True)])

for x in data:
    print(x , " " , data[x])

name   Ram
age   45
isemployed   True"""
"""
for x in data.keys():
    print(x)


name
age
isemployed

for x in data.values():
    print(x)

Ram
45
True


for x,y in data.items():
    print(x, y)


name Ram
age 45
isemployed True


if "age" in data:
    print("present")

data.update({"gender" : "male"})
print(data)
data["age"] = 67
print(data) #{'name': 'Ram', 'age': 67, 'isemployed': True, 'gender': 'male'}

data.pop("gender")
print(data)  #{'name': 'Ram', 'age': 67, 'isemployed': True}
data.clear()
print(data) #{}


####nested dictionary

names={
    "user1":{
            "name" :"Ram",
            "age" : "45",
            "isemployed" :True
    } ,
    "user2":{
            "name" :"sam",
            "age" : "55",
            "isemployed" :True
    }

}

print(names)
#{'user1': {'name': 'Ram', 'age': '45', 'isemployed': True}, 'user2': {'name': 'sam', 'age': '55', 'isemployed': True}}
################################################
#identity operator - compare two objects

# is ,is not
"""
"""
a=[1,2]
b =[1,2]

c=a

print(id(a))   # same val
print(id(b))
print(id(c))  #same val

print(a is c)  #compare two object value  #true
print(a is b)  #false
print(a is not c) #False"""

#####################################################################3
#membership operator To find whether it is a member or not in the list/tuple.dict
"""
a = [21,34,76]

print(21 in a)    #True
print(21 not in a)   #False
"""
###############################################################
#functions -set of code enclosed in a block can be called multiple times

#1 - No return without arguments
"""
def add():
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c =  a+b

add()"""

#2 - No return with arguments
"""
def sub(a,b):
    c = a-b
    print(c)

sub(25,10)
"""

#3 - Return without arguments
"""
def mul():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c= a*b
    return c

#x =mul()
print("Multiplication :" , mul() )
"""

#4 - Return with arguments
"""
def div(a,b):
    c= a/b
    return c

#x =div()
print("Division :" , div(6,3) )
"""

#5 - Arbitrary arguments Function  
"""
def students(*names):
    for name in names:
        print(name)
    print(names)   #('Ram', 'sita', 'mahi', 'Vaishu')-tuple

students("Ram","sita","mahi","Vaishu")
"""

#6 - Keyword arguments function
"""
def message(name , age):
    print(name," age is ",age)

message(age = 23 , name = "anu")
"""

#7 - Arbitrary keyword argument function
"""
def data(**records):
    print(records)    #{'name': 'Anu', 'age': 12, 'gender': 'female'}-dict

data(name = "Anu" , age = 12 , gender ="female")
"""

#8 - Default parameter function
"""
def message(name , city = "Salem"):
    print(name , " is from " , city)

message("ram","nagpur") #ram  is from  nagpu
message("sam") #sam  is from  Salem 
"""

#9 Passing a list as arguement
"""
def total(marks):
    return sum(marks)

print(total([25,10])) #35"""

#10 Recursive function

#a function calling iteslf inside the same function is called recursive function


################lamda function


#################date and time
"""
import datetime as dt

curr_user = dt.date.today()
print(curr_user) #2023-06-15

new = dt.date(2020,3,12)
print(new) #2020-03-12

print(new.year) #2020
print(new.month)#3
print(new.day) #12

time = dt.time(10,30,6,999)
print(time) #10:30:06.000999

print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

curr_time = dt.datetime.now()  #2023-06-15 14:51:08.636131
print(curr_time)

custom_date = dt.datetime(2021,2,9,12,40,23)
print(custom_date.date(),"--------",custom_date.time())#2021-02-09 -------- 12:40:23

#To find the diff between two dates

my_date = dt.datetime.now()
future_date = dt.datetime(2025,6,15)

diff = future_date - my_date
print(diff) #730 days, 8:11:04.348958
my_date = dt.datetime.now()
new = my_date.strftime("%A %b  %d %Y")  
print(new)  #Thursday Jun  15 2023
"""
#########################################################################3
#Math function
"""
import math
print(math.sqrt(25))   #5.0
print(math.ceil(2.5555)) #3  #next whole number
print(math.floor(8.6666)) #8  #number before decimal point

print(math.factorial(5))
print(math.fabs(-7) ) #7  #absolute function will always return positive value
print(math.pow(2,3))    #8   # 2 to the pow of 3 
print(math.pi , math.e)
"""
############################################################################

#TRY block
"""
try:
    a = 10/1
    print(a)
except Exception as e:
    print(e)#division by zero
else:
    print("if there is no exception i will execute ",a)
finally:
    print("irrespective of exception occurs or not , i will execute")
"""
#types of Exception
#print(len(dir(locals()['__builtins__'])))  #158

#Handling multiple exceptions
"""
try:
    a = 10/2
    print(a)
    w = [9,2,4,5]
    print(w[10])
except ValueError :
    print("Value Error Exception")
except IndexError :
    print("Index error Exception")
    """
"""
    5.0
Index error Exception """

##########################################OOPS CONCEPT#####################################

# class = its a blueprint or serves as a template from which individual objects are created.
"""
class Car():
    pass

a = 10
print(type(a)) #<class 'int'>
print(type(Car)) #<class 'type'>

swift = Car()  #instance or object
print(isinstance(swift,Car))   #True
print(type(swift))   #<class '__main__.Car'>
"""

###############class attributes####################

#variables or data in class
"""
class myclass():
    name = "Ram"
    age = 34
#getattr    
#1    
print(getattr(myclass,'name'))  #Ram
#2
print(myclass.name) #Ram
print(myclass,'gender','gender not found') #gender gender not found

#setattr

setattr(myclass,'name','Vaishali')
print(myclass.name) #Vaishali

setattr(myclass,'gender','female')
print(myclass.gender) #female
#delattr(myclass,'name')
print(myclass.name)

myclass.city = "chennai"
print(myclass.city) #chennai

#to see attributes in class

print(myclass.__dict__)

#To delete attr in class
print(myclass ,'name' , 'name not found')
#delattr(myclass,'city')
#print(myclass ,'city' , 'city not found')
del myclass.age
print(myclass.age)
"""

#######################################instance attributes#####################
"""
class User:
    course = "java"

print(User.__dict__)
obj1 = User()
print(obj1.__dict__) #{}
print(obj1.course ) #java
#first it will search in its dict , as it is not there , it will fetch from its main class
obj1.course = "python"
print(obj1.__dict__)  #{'course': 'python'}

"""
#############################class methods##########################
"""
class Movie:
    seat_no = 4
    show = "morning"

    def ticket():
        print("Seat No : ",Movie.seat_no)
        print("Show type : ",Movie.show)
#1
Movie.ticket()
#Seat No :  4
#Show type :  morning


#2
print(getattr(Movie,'ticket'))
getattr(Movie,'ticket')()

#Seat No :  4
#Show type :  morning

#3

Movie.__dict__['ticket']()
#Seat No :  4
#Show type :  morning
"""

###################################################################################
#init method

#its a contructor method and will be called when new object is created for that class
#used for value initialization purpose
"""
class Team:
    def __init__(self):
        print("will be called when new instance is created")
    
o1 = Team()#will be called when new instance is created
"""
"""
class Meeting:
    def __init__(self,time):
        self.time = time

    def printall(self):
        print("Meet time ",self.time)

o2 = Meeting(10)
o2.printall()  #Meet time  10
"""

############################################################
#property decorator
"""
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def msg(self):
        return self.name + " is " + str(self.age) +" years old"


o1 = User('vaishu',29)
print(o1.name , o1.age , o1.msg())
o1.age = 45
print(o1.msg())"""

#property decorator getters and setters
"""
class Student:
    def __init__(self,total):
        self.total = total
    def average(self):
        return self.total/5.0
    
o1 = Student(450)
print(o1.total)   #450
print(o1.average())  #90

o1.total = 250
print(o1.total)   #450
print(o1.average())  #90
"""

#class method decorator
"""
class Student:
    count =0
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        Student.count +=1

    def print_details(self):
        print(self.name , " ", self.age)

    @classmethod
    def total(cls):
        print("Total :" , cls.count)

o2 = Student("Vaishu",29)
o2.print_details()


o3 = Student("Raja",23)
o3.print_details()
Student.total()
"""

####################################################################33
#static method in python
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_details(self):
        print(self.name , self.age)

    @staticmethod
    def welcome():
        print("Welcome")

s1 = Student("Vaishu",29)
s1.print_details()
s1.welcome()

s2 = Student("saravanan",33)
s2.print_details()
s2.welcome()
"""

################################################################################
#Data Abstraction - providing only essential information outside and hiding background details

#Encapsulation - is the process of wrapping data and code into a single unit eg:class

#Example
"""
class Library:
    def __init__(self,books):
        self.books = books

    def list_books(self):
        print("Available books in library:")
        for book in self.books:
            print(book)

    def borrow_books(self,borrow_book):
        if borrow_book  in self.books:
            print("get your book")
            self.books.remove(borrow_book)
        else:
            print("Book not available")

    def receive_books(self,receive_book):
        print("You have received the book")
        self.books.append(receive_book)

books = ["c","c++","java","python"]
obj = Library(books)

msg = """
#1.show available books
#2.borrow books
#3.return books
"""
while True:
    print(msg)
    ch = int(input("Enter your choice: "))
    if ch== 1:
        obj.list_books()
    elif ch== 2:
        book = input("Enter book name to borrow : ")
        obj.borrow_books(book)
    elif ch == 3:
        book = input("Enter book name to return: ")
        obj.receive_books(book)
    else:
        print("Thanks! Come Again")
        quit()
"""

########################################################################################3
#INHERITANCE

#Single inheritance- derived class is inherited from only one base class
"""
class Nokia:
    company = "Nokia-India"
    website = "www.nokia-india.com"

    def contact_details(self):
        print("Address:- Adams Road , New York")

class Nokia1100(Nokia):    #single inheritance
    def __init__(self):
        self.name = "Nokia1100"
        self.year = 1990

    def product_details(self):
        print("Company : " , self.company)
        print("Website : " , self.website)
        print("Name : " , self.name)
        print("Year : " , self.year)


obj = Nokia1100()
obj.product_details()
obj.contact_details()
"""

######### multiple inheritance

#A class can inherit the properties of nore than one parent class
"""
class Father:
    def learn_chess(self):
        print("chess learning from father")
    def learn_fishing(self):
        print("learn fishing")

class Mother:
    def learn_chess(self):
        print("chess learning from mother")
    def learn_cooking(self):
        print("learn cooking")
    

class Daughter(Father,Mother):
    def learn_cycling(self):
        print("knows cycling")

obj = Daughter()
obj.learn_cycling()
obj.learn_fishing()
obj.learn_cooking()
obj.learn_chess()

#O/P

#knows cycling
#learn fishing
#learn cooking
#chess learning from father  - this is due to father class is given first in the daughter class during inheritance


"""
############################ multilevel  inheritance##############
"""
class1
|
class2
|
class3
"""
"""
class Grandfather:
    def own_house(self):
        print("own a house")

class Father(Grandfather):
    def own_bike(self):
        print("own a bike-Father")

class Son(Father):
    def own_car(self):
        print("own a car")
    def own_bike(self):
        print("own a bike-Son")

obj = Son()
obj.own_car()
obj.own_house()
obj.own_bike()


#O/P

#own a car
#own a house
#own a bike-Son

"""

######################## function overriding##################

#a method having same method name in both base class  and derived class but different method body

"""
class Employee:
    def working_hrs(self):
        self.working_hrs = 50

    def print_working_hrs(self):
        print("working hours : " , self.working_hrs)

class Trainee(Employee):
    def working_hrs(self):
        self.working_hrs = 60

    def print_working_hrs(self):
        print("working hours : " , self.working_hrs)

    def reset_hrs(self):
        super().working_hrs()


emp = Employee()
emp.working_hrs()
emp.print_working_hrs()

trainee = Trainee()
trainee.working_hrs()
trainee.print_working_hrs()
trainee.reset_hrs()
trainee.print_working_hrs()

 """

 ###################### Diamond problem
"""
class A:
    def display(self):
      print("Am the display of class A")

class B(A):
    def display(self):
      print("Am the display of class B")

class C(A):
    def display(self):
      print("Am the display of class C")

class D(B,C):
    def display(self):
      print("Am the display of class D")
      
obj = D()
obj.display()

"""

############################ Operator overloading

#this comes under polymorphism

"""
a = 10
b = 20

print(a+b)

g = "Automation"
h = "Tester"

print(g+h)"""
"""
class Addition:
    def __init__(self,a):
        self.a = a

    def __add__(self,a):
        return obj1.a+obj2.a
    
    def __sub__(self,a):
        return obj1.a-obj2.a

obj1 = Addition(10)
obj2 = Addition(20)

print(obj1+obj2)
print(obj1-obj2)
"""

#################################### ABSTRACTION
"""
from abc import ABC , abstractmethod

class Bank(ABC):      #inherits abstract base class

    @abstractmethod
    def credit(self):
        pass

    @abstractmethod                    #method which is not defined is abstract
    def loan(self):
        pass

    @abstractmethod
    def debit(loan):
        pass

class HDFC(Bank):
    def credit(self):
        print("HDFC provide credit")    #the class which is extending abstract class should implement all the abstract method

    def debit(self):
        print("HDFC provide debit")

    def loan(self):
        print("HDFC provide loan")

obj = HDFC()
obj.loan()
obj.credit()
obj.debit()                        

#HDFC provide loan
#HDFC provide credit
#HDFC provide debit
"""
################################################################################
# File Handling
"""
try:
    myfile = open("C:\\Users\\VBASKA13\\Desktop\\vaishu.txt","r")
    #print(myfile.read()) will read all
    #print(myfile.readline())  #will oread only first line
    #print(myfile.readline(2) )  # second line with only two characters
    print(myfile.readlines())  #['Automation tester\n', 'I  am from chennai']
except FileNotFoundError:
    print("Error : File not found")
else:
    myfile.close()

"""

############ file reading line by line using loop
"""
myfile = open("C:\\Users\\VBASKA13\\Desktop\\vaishu.txt","r")
for line in myfile:
    print(line)
"""
#Automation tester

#I  am from chennai 

############# file write
"""
myfile = open("C:\\Users\\VBASKA13\\Desktop\\vaishu.txt","w") #write
myfile = open("C:\\Users\\VBASKA13\\Desktop\\vaishu.txt","a") #append
myfile.write("\nWorking in Tech mahindra")
myfile.close() """

############################ Delete file
"""
import os

if os.path.exists("C:\\Users\\VBASKA13\\Desktop\\vaishu.txt"):
    os.remove("C:\\Users\\VBASKA13\\Desktop\\vaishu.txt")   # deletes file
else:
    print("file not found")

#folder remove
os.rmdir("foldername")"""

#Remove vowels from a string
"""
mystring = "ahjjff enbcig hjobbubbt"
a = list(mystring)
vowels = ['a','e','i','o','u']

for letter in a:
    if letter in vowels:
        a.remove(letter)

out = "".join(a)
print(out)"""

"""
mystring = "ghagh ghjgfejghjj bminb vbnboqa bmbub"
vowels = ['a','e','i','o','u']
mylist = list(mystring)

for letter in mylist:
  if letter in vowels:
      mylist.remove(letter)

final_string = "".join(mylist)
print(final_string) """



















































































































