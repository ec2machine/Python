#File handling - :
# r => read, w => write(replace), 
# a => append(add with exits data), x => create file

import os
# #create
os.remove('helloworld.txt')

file=open('helloworld.txt',"x",)
file.write('helloworld')
file.write("hello")
file.close()


# #read
file=open('hello.txt','r')
print(file.read())
file.close()

# #write
file=open("hello.txt",'w')
print(file.write("hello vigneshwaran m"))


# #append
file=open("hello.txt",'a')
print(file.write("gfdghjdfjkshds"))
file.close()


#with ---> this auto close file
with open("world.txt",'w+') as demo:
    demo.write('hwllo world')
    demo.seek(0)
    print("deemo file print:",demo.read())
 

