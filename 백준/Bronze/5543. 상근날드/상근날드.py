burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
cola = int(input())
cider = int(input())

min_burger = min(burger1, burger2, burger3)
min_drink = min(cola, cider)

set_price = min_burger + min_drink - 50

print(set_price)
