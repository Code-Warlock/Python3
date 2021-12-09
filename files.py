""" Files I/O """

# stdio === > Standard Input and Output
# stdin and stdout


# name = input("Enter your name : ")
# print(name)
# Opening files in read mode
# Binary // Normal
# f = open("words.txt","r")
# read and the readlines methods
# print(f.readlines())
# print(f.read())

# print(f.read(10))
# print(f.read())
# f.seek(0)
# print(f.read())
# f.seek(15)
# print(f.read())

# Opening files in write mode

# f = open("words.txt","w")
#
# # write and writelines methods
#
# f.write("I have changed the content of this file!")
#
#
# f.close()
#
#
#
# f = open("words.txt")
#
# print(f.read())
#
# f.close()


# Opening files in read and write mode
# f = open("samaraksa.txt","w")
# # read , readlines , write and writelines
#
# # f.write("Michael used the read/write mode!!!!\n")
# f.write("Michael used the read/write mode!!!!\n")
#
# # print(f.read())
# f.close()

# # Opening files in create mode
# f = open("samaraksa.txt","x")
# # read , readlines , write and writelines
#
# # f.write("Michael used the read/write mode!!!!\n")
# f.write("Michael used the read/write mode!!!!\n")
#
# # print(f.read())
# f.close()


# Opening files in the append mode


# f = open("samar.txt","a+")
# # read , readlines , write and writelines
#
# # f.write("Michael used the read/write mode!!!!\n")
# f.write("Mubarak and Samuel used the read/write mode!!!!\n")
# f.seek(0)
# x = f.read()
# print(x)
# # print(f.read())
# f.close()




with open("words.txt" ,"a+") as f:
    print(f.read())



print(f.read())
