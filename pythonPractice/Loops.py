#while loop
count=0
while(count<3):
    print("hello world")
    count=count+1
print("-------------")

#for loop
name= ("java", "python", "dot net", "C sharp")
for i in name:
    print(i)

print("-------------")

str="i love python"
for i in str:
    print(i)

print("-------------")

list =["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])

print("-------------")
#nested for loop
for i in range(1,5):
    for j in range(i):
        print(i, end="")
    print(i)

print("-------------")

#break and continue

str= ["python", "java", "C sharp"]
for l in range(len(str)):
    print(str[l])
    if (str[l]=="java"):
        print("hey i found java")
        break
