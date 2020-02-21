#-*- coding:utf-8 -*-

def basicConceptOfVariable():
	'''
	Watch the basic conecpt of variables

	You can contain value in varaible that you named
	'''
	num1 = 100
	num2 = 300
	print(num1+num2)

def conceptOfVariableInPython():
	'''
	In python, variable is not a box containing value
	It is closer to the pointing arrow than the box
	'''

	list1 = [1,2,3,4]
	list2 = list1
	print(list1 == list2)
	# == in lists : 
	# Returns True,
	# if all elements and order of elements are same between two lists

	list1[0] = "hi"
	print(list1)
	print(list2)
	print(list1 == list2)
	# it will return True
	# because list1 and list2 are pointing to same object ["hi",2,3,4]

	# The id of list1 is same with the id of list2
	print("id of list1 : {}".format(id(list1)))
	print("id of list2 : {}".format(id(list2)))

def whatIsList():
	'''
	list is the container that is able to contain various objects
	it is iterable and you can access the element in list by index number
	it guarantees the sequence of elements.
	'''
	list1 = [100,20,33,44,55,-1,10,11,23,55]
	list2 = [1,2,0,"hi",("it is","tuple object"), ["list", " in", "list"] ]
	print("list1: {}".format(list1))
	print(list1)
	print(list1[0])
	print(list1[0:3])
	print(list1[3:])
	print(list1[:-1]) 
	print(list1[3:-2])
	print(list1[::-1]) #you can get reversed list
	print(list1[::2]) #you can get elements whose indices are even

	print("\n")
	print("list2: {}".format(list2))
	print(list2[0])
	print(list2[-1])
	print(list2[-1][1])
	print(list2[4])
	print(list2[4][0])

def howCanCopyTheObject():
	'''
	Use 'copy()'function
	'''

	list1 = [1,2,3,4]
	list2 = list1.copy()

	list1[0] = "hi"
	print(list1 == list2)
	print(list1)
	print(list2)
	# it will return False
	# because list1 and list2 are pointing to different objects

	# The id of list1 is different from the id of list2
	print("id of list1: {}".format(id(list1)))
	print("id of list2: {}".format(id(list2))) 

def setIsGreat():
	'''
	if you can use 'set' properly, 
	'if-else' statement can be replaced by 'set'
	'''
	set1 = {1,2,3,4,5} # == set([1,2,3,4,5])
	set2 = {3,4,5,6,7,8,9,10,200}
	# [CAUTION!] 
	# 'set' type does not guarantee the sequence of elements

	# 'set' type works like the set in mathematics
	print(set1)
	print(set2)
	print(set1 & set2)
	print(set1 | set2)
	print(set1 - set2)
	print(set2 - set1)


# Run the function below by erasing the first character '#' of each lines

#basicConceptOfVariable()
#conceptOfVariableInPython()
whatIsList()
#howCanCopyTheObject()
#setIsGreat()
