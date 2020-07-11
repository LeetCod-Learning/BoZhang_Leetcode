import sys
# 递归算法
# 最大公约数and 最小公倍数（两数相乘/最大公约数）
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)



while True:
    try:
        n = sys.stdin.readline().strip()
        n = n.split()
        a = int(n[0])
        b = int(n[1])
        i,j = a,b
        m =a%b
        while m != 0:
            a = b
            b = m
            m =a%b
        print(a)

    except:
        break



