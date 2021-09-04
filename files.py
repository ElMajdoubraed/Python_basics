#read file
my_file=open("file.txt","r")
#print(my_file.read())
#print(my_file.readline())
#print(my_file.read(3))#read 3 caracteres
"""
for line in my_file:
    print(line)
my_file.close()
"""
print(my_file.readlines())#list
#close file
my_file.close()

#create new file and writing
new_file=open("newfile.txt",mode="w",encoding="utf-8")
for i in range (5) :
         new_file.write("new line "+str(i+1)+"\n")
new_file.close()
#append
a=["new line 5\n","new line 6\n"]
new_file=open("newfile.txt",mode="a+",encoding="utf-8")
new_file.writelines(a)
new_file.close()
