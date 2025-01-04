"""for i in range(10):
    print(i+1)

print("#####################")


for i in range(1,11):
    print(i)
"""


## 369 게임

for i in range(1,101):
    if i//10 == 3 or i//10 == 6 or i//10 == 9:

        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            print("짝짝")
        else:
            print("짝")
    else:
        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            print("짝")
        else:
            print(i)