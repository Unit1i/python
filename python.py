# num = [45,78,87,95,87,45,100,10,90,800]
#1 # for x in num:
#     if num % 100 ==0:
#         print(x)


#2 # x = max(num)
# y = min(num)
# print(x+y)

#3 # num = [7,8,5,4,9,7,10,11,15,14]
# num1 = 0
# for x in num:
#     if x > 5:
#         num1 += x
# print(num1)

#4 # num = [14,57,47,524,45,800,440,774,100,120,]
# num1 = []
# for x in num:
#     if x % 3 ==0 and x % 4 != 0:
#         num1.append(x)
# print(len(str(x)))

num = [38,91,50,87,73,74,46,45,13,92]
y = 0
for x in num:
    if num[y] - num[y+1] > 10 or num[y] - num[y+1] < -10:
        print(num[y])
    y += 1
