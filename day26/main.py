file1=open("file1.txt","r")
zz=file1.readlines()
stripped1=[int(text.strip()) for text in zz]

file2=open("file2.txt","r")
ww=file2.readlines()
stripped2=[int(text.strip()) for text in ww]

result=[n for n in stripped1 if n in stripped2]
print(result)




