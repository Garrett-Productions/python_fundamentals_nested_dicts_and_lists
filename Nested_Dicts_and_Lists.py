#1. Update Values in dictionaries and lists

x = [ [5,2,3],
    [10,8,9] 
    ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

players = [
    {'first_name': 'Garrett', 'last_name': 'Turner'}
]

print(players[0]['last_name'])
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

print(x[1][0]) #this shows I targeted the right value
x[1][0] = 15 #this is the syntax to change the value
print(x) #this gets our desired outcome #1 of question 1 is answered

print(students[0]['last_name']) #we have targeted the correct name
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name']) #Here we have changed the name from Jordan to Bryant
#this answers the 2nd part of the 1st question

print(sports_directory['soccer'][0]) #we have accessed the right position in our directory
sports_directory['soccer'][0]= 'Andres'
print(sports_directory['soccer'][0]) #here we have changed the name of Messi to Andres
#this answers the 3rd part of the 1st question

print(z[0]['y'])
z[0]['y'] = 30
print(z) #here we have changed the value of the 'y' key to 30
#this answers the 4th part of the 1 question

#-----------------------------------------------------------------------------

#example list of dictionaries below 
users = [
    {"first": "Garrett", "last" : "Turner"}, #index0
    {"first": "Matt", "last" : "Wehner"}, #index1
    {"first": "Jay", "last" : "Patel"} #index2
]


#-----------------------------------------------------------------------------

#2.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#------------Here is the first example----------#

def iterateDictionary(students):
    for i in range(len(students)):
        for key in students[i]:
            print(students[i])
        print("")
        
iterateDictionary(students)

#------------Here is the second example----------#

def iterateDictionary(list):
    for dict_item in students:
        for key in dict_item:
            print(dict_item[key])

iterateDictionary(students)
#-------------------------------------------------

#3.Get Values From a List of Dictionaries
users = [
    {"first": "Garrett", "last" : "Turner"}, #index0
    {"first": "Matt", "last" : "Wehner"}, #index1
    {"first": "Jay", "last" : "Patel"} #index2
]

def iterateDictionary2(key_name, some_list):
    for index in some_list:
        for key, value in index.items():
            if key == key_name:
                print(value)
    print("")

iterateDictionary2("first", users)
iterateDictionary2("last", users)

#--------------------------------------------------

#4.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict): 
    for key in some_dict: 
        #print(key)
        print(key,len(some_dict[key]))  
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
        print("")


printInfo(dojo)

#for eack key in dojo we are going to print the length. notes notes notes

def iterateDictionary2(key_name, some_list):
    for index in some_list:
        for key, value in index.items():
            if key == key_name:
                print(value)
    print("sup")

iterateDictionary2("first", users)