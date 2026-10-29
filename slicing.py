str = "apna college"
print(str[0:4]) 
# last idex tak jane ke liye ham print
print(str[0:len(str)])


##nagative index print
str = "Apple"
print(str[-5:-1])


##string function
str = "I am studying python from Apnacollege"
print(str.endswith("apna"))

#capitalize means ki firt letter capital hona chahiye
str = "i am studying python from apnacollege"
print(str.capitalize())

## replace function
str = "i am studying python from ApnaCollege"
print(str.replace("python", "css"))

##find function
str = "i am studying python from ApnaCollege"
print(str.find("from"))

##count function ## ye batata h ki from pure sentance me kitni br aaya h
str = "i am studying python from ApnaCollege"
print(str.count("from")) 

##qution practicwe 
name = input("enter yout name: ")
print("length of your name is", len(name))

## qution
str = "Hi, $Iam the $ symbol $99.99"
print(str.count("$"))