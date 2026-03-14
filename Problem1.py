numbers = list(range(1,51))
print(numbers, end=" ")

# def filteredSquare(numbers):
#     for elements in numbers:
#         if elements % 2 == 0:
#             print(elements, end = " ")
#         else:
#             continue

# filteredSquare(numbers)   

Filtered_Square_Even = [i**2 for i in range(1, 51) if i % 2 == 0]
print(Filtered_Square_Even)