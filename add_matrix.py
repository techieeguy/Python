#Python program to add two Matrices
first = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print("\nEnter the elements of first matrix:")
for i in range(len(first)):
   for j in range(len(first[0])):
       first[i][j] = int(input(">"))

second = [[0,0,0],
          [0,0,0],
          [0,0,0]]

print("\nEnter the elements of second matrix:")
for i in range(len(first)):
   for j in range(len(first[0])):
       second[i][j] = int(input(">"))

add = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(first)):
   for j in range(len(first[0])):
       add[i][j] = first[i][j] + second[i][j]

print("\nAddition of two Matrices:\n")
for r in add:
   print(r)

# Follow @techieeguy for more.