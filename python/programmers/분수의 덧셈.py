def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = (denom2 * numer1) + (denom1 * numer2)
    denom = denom1 * denom2

    gcd_value = gcd(denom, numer)

    answer.append(numer // gcd_value)
    answer.append(denom // gcd_value)

    return answer



print(solution(1, 2, 3, 4))


