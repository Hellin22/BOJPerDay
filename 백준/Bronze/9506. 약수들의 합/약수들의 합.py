n = int(input())

while n != -1:
    divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
    sum_divisors = sum(divisors)
    
    if sum_divisors == n:
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
    
    n = int(input())
