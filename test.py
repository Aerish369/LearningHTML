num = int(input("Enter a numbeer:"))
sum = 0
for i in str(num):
    b = int(i) ** len(str(num))
    sum += b

if num == sum:
    print("True")
else:
    print("False")


