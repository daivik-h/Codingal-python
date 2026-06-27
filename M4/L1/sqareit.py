
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


even_squares = []
odd_squares = []


for num in range(start, end + 1):
    square = num ** 2  
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)


print(f"Even square values: {even_squares}")
print(f"Odd square values: {odd_squares}")