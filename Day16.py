# File Handling (open a file and read and use the content in program
# open a file and write the content)
# Done by Abhiyan Shrestha

# Flow of reading file
# Open the file
# Content read
# content use
f= open('Abhiyan Shrestha Python Coding Skills from basic to advance\hello.txt','r')
a = f.read()
print(a)
f.close()

g = open('Abhiyan Shrestha Python Coding Skills from basic to advance\hello.txt','w')
g.write('Hello this data is writen from program')
g.close()

h = open('Abhiyan Shrestha Python Coding Skills from basic to advance\hello.txt','w')
h.write('Hello this data is writen from program')
h.close()

