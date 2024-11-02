

"""num = -1

while num > 100 or num < 0:
    num = int(input("수학 점수는?"))



if num > 80:
    print("A반")
elif num > 60:
    print("B반")
else:
    print("C반")
    """
import random

answer = int(random.randrange(1,100))
um = int(input("어떤 숫자인지 1에서 100까지의 수중 하나를 선택하세요"))
print(answer)
while answer != um :
    answer = int(random.randrange(1, 100))
    um = int(input("어떤 숫자인지 1에서 100까지의 수중 하나를 선택하세요"))
    print(answer)
if answer == um :
     print("good")



