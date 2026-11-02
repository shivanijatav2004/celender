##sets unorederd h
collection = {1, 2, 2, 2, "hello", "world", "world", 4} ## string value bhi add kr skte h
print(collection)
print(type(collection))
print(len(collection))#total num of items

##empty set(dictiinary) empty set; dictionary sytanx
collection = set()
print(type(collection))


##add method
collection = set()
collection.add(1)
collection.add(2)
collection.add(2) #string bhi pass kr skte h
collection.add("Shivani")
#tuple bhi pass kr skte h
collection.add((1, 2, 3)) ##list ko pass nhi kr skte
##remove
collection.remove(2)
print(collection)


##clear method
collection.clear()
print(len(collection))

##pop value random value remove krta h ye
collection = {"hello", "world", "apnacollege", "codeing", "python"}
print(collection.pop())
print(collection.pop())

##unio method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1)
print(set2)

##intersection method common value return krtah
print(set1.interssection(set2)) #{2, 3}
