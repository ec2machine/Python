#String - indexed, methods, formating

name='vigneshwaran'
age=22
hight=145.650090

print(name)

print(name[0])  # call index show element

print(f"Hello this {name}")  #Called F sting method 

print("Hello this my name {} my age is {}".format(name,age))  
# use format funtion {} -use this, pass argement var name

print("Hello world my name is %s, my age is %d" %(name, age))

#f sting method use sjow only 2 decimal value, this not or int value
print(f"{hight:.2f}")  

#sting with symbols
a="hello"
b="world"
print(a+b) # add to sring
print(a*3) # multiple thaT WORD

#String Funtions:
print(a.isalpha())   # true or false

print(b.isdigit())    #true or fale

print(a.isalnum())   #true or fale both or one inside

print(a.islower())

print(b.isupper())

print(a.upper())

print(a.lower())

print("hello world".title())

c="Hwllo worlD".swapcase()  #upper to locaer, lower to upper
print(c)

# d=str(input("enter some words:"))   # remote that char returen list
# print(str(d.split(",")))

e=["hwllo", "workd"]  # this join use two sting or list of elemt join 
print("-".join(e))  # "-" ===> this between of two elemts

print("hwlloworld".replace("w","e"))   # this replace the elemnt find and replace
# f=["hwllo","world"]

# F= (list(map(lambda i:i.replace("w","--"),f))) 
# G=("@@".join(F))
# print(G, type(G))

# f=["hwllo","world"]
# g=" ".join(f)
# print(g, type())

print("helloeee".count("e"))  #count char

print('hello'.index("e")) # find char is index

print("hellollo".find("o"))  # find chr index but fisrt chr only show

print("  hellow".strip()) # remove unvanatend   spcae for left and right
print("  hellow".lstrip())
print("  hellow".rstrip())



 





