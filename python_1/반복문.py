

"""num = -1

while num > 100 or num < 0:
    num = int(input("수학 점수는?"))

ques = str(input("어디 쪽으로 이동 할까요?"))

if num > 80:
    print("A반")
elif num > 60:
    print("B반")
else:
    print("C반")
    """
#1~100 숫자 맞추기
"""import random

answer = int(random.randrange(1,100))
um = int(input("어떤 숫자인지 1에서 100까지의 수중 하나를 선택하세요"))
print(answer)
while answer != um :
    answer = int(random.randrange(1, 100))
    um = int(input("어떤 숫자인지 1에서 100까지의 수중 하나를 선택하세요"))
    print(answer)
if answer == um :
     print("good")"""

# 피보나치 수열

"""pibo = ""
pibo = 1
while pibo < 100 :
    pibo = pibo + pibo
    print(pibo)"""

"""count = int(input("숫자 하나를 입력해라"))
i = 0
while i < count :
    print("*")
    i = i + 1

"""

x = 0
y = 0
print((x,y))
ques = ""
ques = str(input("어디 쪽으로 이동 할까요?"))
while x <= 100 and y <= 100:
    if ques == "LEFT":
     x = x - 1
     print((x,y))
    elif ques == "UP":
     y = y + 1
     print((x,y))
    elif ques == "RIGHT":
     x = x + 1
     print((x,y))
    elif ques == "DOWN":
     y = y - 1
     print((x,y))