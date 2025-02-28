total_price = int(input())  
sum_of_9_books = 0

for _ in range(9):
    sum_of_9_books += int(input())

missing_price = total_price - sum_of_9_books

print(missing_price)
