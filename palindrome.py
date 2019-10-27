#Keshav Agrawal
#To check for palindrome
s = input()
sum = 0
i = 0
while i <len(s):
    if s[i] == s[len(s)-1-i]:
        sum += 1
    i +=1
if sum == len(s):
    print("Yes")
else:
    print("No")
