import sys
inp = sys.stdin.readline

munser = inp().strip()
find_str = inp().strip()
res = 0
i = 0
while(i<=len(munser) - len(find_str)):
    if munser[i] != find_str[0]: 
        i+=1
        continue
    flag = True
    # 맞기 때문에 시작해야함.
    for j in range(len(find_str)):
        if(munser[i+j] != find_str[j]): 
            flag=False
            i+=1
            break
    if(flag == False): continue
    res+=1
    i += len(find_str)

print(res)

