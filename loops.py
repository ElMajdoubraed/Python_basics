# while loop
i = 0
while i < 5:
    print(i)
    i += 1
    #i=i+1

# while loop with break
i=0
while i < 5:
    print(i)
    if i == 3:
         break
print("end")
# while loop with continue
i=0
while i < 5:
    if i == 3:
         continue
    print(i)
print("end")
# for loop

for i in range(5):
    print(i)

for i in range(10, 13):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)
