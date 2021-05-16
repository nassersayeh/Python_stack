#Update Values in Dictionaries and Lists
'''
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]["last_name"] = "Bryant"
print(students[0])
sports_directory ['soccer'][0] = "Andres"
print(sports_directory['soccer'])
z[0]['y'] = 30
print(z[0]['y'])'''

#Iterate Through a List of Dictionaries
'''
def iterateDictionary(lis):
    for i in range(len(lis)):
        print("first_name - "+lis[i]['first_name']+", last_name - "+ lis[i]['last_name'] )

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) '''

#Get Values From a List of Dictionaries
'''
def iterateDictionary2(key,lis):
    for i in range(len(lis)):
        print(lis[i][key])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2("first_name", students)'''

#Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printIndo(lis):
    a = []
    b=[]
    counter1 = 0
    counter2 = 0
    for i in range(len(lis['locations'])):
        a.append(lis["locations"][i])
        counter1+=1
    print(counter1 , " Location \n" , a)
    for i in range(len(lis['instructors'])):
        b.append(lis['instructors'][i])
        counter2 +=1
    print(counter2,"instructors \n",b)


printIndo(dojo)