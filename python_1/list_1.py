
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(a[0])
print(a[1])

print(a[0:7]) #a[N:M] n번째부터 M-1 번째까지

b = ["test", 1.4, 251, "Aaddas"]

c = [[100,100,99,88,100],[100,78,85,45,96],[70,77,10,89,100]]
d = [[[19,15,50,68,94],100,100,99,88,100],[100,78,85,45, 96],[70,77,10,89,100]]

print(c[0][2])
print(c[1])
print(c[0][2:])
print(c[1:])

print("++++++++++++++++++++++++++++++++++++++++++++++++")
e = [13, 12, 61, 23, 16]
f = e

e[1] = 10
print(e)
print(f)

g = a + c
print(g)

h = a * 5
print(h)

print(len(a))
print(len(b[0]))

print("==========================================")

text = " Hello my frineds"
print(text[4])
print(text[4:])
