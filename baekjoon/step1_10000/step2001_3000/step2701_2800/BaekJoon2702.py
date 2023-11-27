num = int(input())
answer = ""

def T(a, b):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b, gcd_value):
        return (a * b) // gcd_value

    gcd_result = gcd(a, b)
    return str(lcm(a, b, gcd_result)) + ' ' + str(gcd_result)

for _ in range(num):
    a, b = map(int, input().split())
    answer += T(a, b) + "\n"

print(answer)