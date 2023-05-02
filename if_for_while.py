score = int(input("Enter score: "))

if score >= 80:
  print("Score is great!")
elif score >= 60:
  print("Score is good!")
else:
  print("Score is not great...")

for i in range(10):
  print(i)
for i in range(5, 10):
  print(i)
for i in range(1, 10, 2):
  print(i)

numbers = [11, 22, 33, 44, 55]
for number in numbers:
  print(number)

for x in range(1, 10):
  for y in range(1, 10):
    print(str(x) + ' × ' + str(y) + ' = ' + str(x * y))

weight = 60
while weight < 70:
  print(weight)
  weight += 1