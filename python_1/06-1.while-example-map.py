X = ""
Y = ""
X = 0
Y = 0
ques = ""
ques = str(input("Where do you want to move?"))
while ques != "UP" or "DOWN" or "LEFT" or "RIGHT":
    input("Where do you want to move?")
if ques == "UP":
  X = X
  Y = Y + 1
  print((X,Y))
if ques == "DOWN":
  X = X
  Y = Y - 1
  print((X, Y))
if ques == "LEFT":
  X = X - 1
  Y = Y
  print((X,Y))
if ques == "RIGHT":
  X = X + 1
  Y = Y
  print((X,Y))