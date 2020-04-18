import easygui as g
n = g.enterbox("首项")
 
sum = 0
print ("首项：")
counter = int(input())
while counter <= int(n):
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
input()





'''
print ("请输入末项：")
n = input()
sum = 0
print ("请输入首项：")
counter = input()

print ("请输入公差：")
a = input()

while counter <= n:
    sum = sum + counter
    counter += 1

#print ("counter + %d的和为：%d" % (n,sum))
print ((n,sum))
input()
'''