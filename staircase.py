def staircase(n):
    # Write your code here
    number = n
    string = "#"
    espace = " "
    for i in range(1, number+1):
        print(f'{espace * (number-i)}{string * i}')

staircase(6)