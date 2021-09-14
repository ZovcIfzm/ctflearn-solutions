'''
Can you help me? I need to know how many lines there are where the 
number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. 
Please! Here is the file: https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys
'''

data_file = open("data.dat", 'r')
lines = data_file.readlines()

count = 0

for line in lines:
    numOnes, numZeros = 0, 0
    for char in line:
        if char == '0':
            numZeros += 1
        elif char == '1':
            numOnes += 1

    if numZeros % 3 == 0 or numOnes % 2 == 0:
        count += 1

print(count)
