t = int(input())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

for _ in range(t):
    n = list(map(int, input().split()))
    ncount = len(n)
    gcd_sum = 0

    for i in range(1, ncount):  
        for j in range(i+1, ncount):  
            gcd_sum += gcd(n[i], n[j])  


    print(gcd_sum)
