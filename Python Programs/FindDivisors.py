#This program find the divisors of a given number and says iff it's prime or not
def divisors1(i):
    div = []
    for x in range(2,i-1):
        if i%x == 0:
            div.append(x)
    if len(div) == 0:
        return (str(i) + " is prime")
    else:
        return div

def divisors2(num):
        l = [a for a in range(2, num) if num % a == 0]
        if len(l) == 0:
            return str(num) + " is prime"
        return l