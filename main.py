import math


def multiplesOf3or5():
    mul5 = 0
    mul3 = 0
    sum = 0
    sum5 = 0
    while (mul3 + 3 < 1000):
        mul3 += 3
        print(mul3)
        sum += mul3
        print(sum)
    print("sum: ", sum)
    while (mul5 + 5 < 1000):
        mul5 += 5
        if not (mul5 % 3 == 0):
            sum5 += mul5
    print("sum5: ", sum5)
    return sum + sum5


def compute():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)


def evenFibonacci():
    fib = [1, 1]
    i = 2
    while (i < 4000000):
        fib.append(i)
        i += fib[-2]
    ans = sum(x for x in fib if (x % 2 == 0))
    return ans


def bigPrime(num):
    # 600851475143
    n = num
    prime = [2, 3, 5, 7]
    for i in range(0, 20):
        prime.append(nextprime(prime))

    while not (n in prime):
        for x in prime:
            while (n % x == 0):
                n //= x
        for i in range(0, 3):
            prime.append(nextprime(prime))
    return n


def nextprime(prime):
    n = prime[-1]
    bool = True
    # list = []
    while (bool):
        n += 1
        # list.extend(n % x != 0 for x in prime)
        if all(n % x != 0 for x in prime):
            return n


def isPalindrome(num):
    n = num
    reversed = 0
    while (n > 0):
        reversed *= 10
        reversed += n % 10
        n //= 10
    return num == reversed


def bigPalindromeProd(num1, num2):
    prod = num1 * num2
    while not (isPalindrome(prod)):

        if (((num1 - 1) * num2) >= ((num2 - 1) * num1)):
            num1 -= 1
        else:
            num2 -= 1
        prod = num1 * num2
    return [num1, num2]


def bigPalindrome():
    lst = []
    for x in range(999, 400, -1):
        for y in range(999, 400, -1):
            # prod = x * y
            if isPalindrome(x * y):
                lst.append([x, y])
    list = []
    list.extend([x * y, x, y] for (x, y) in lst)
    return max(list)


def smallestMult():
    lst = []
    lst.extend(x for x in range(2, 21))
    i = 2520
    while not (all(i % x == 0 for x in lst)):
        n = max(x for x in lst if i % x != 0)
        # print("max un divable: ",n)
        # print("incremanter:    ", n - i % n)
        i += n - i % n
    return i


def smallmult():
    ans = 1
    for i in range(1, 21):
        ans *= i // math.gcd(i, ans)
    return str(ans)


def sumDiff():
    sumOfSq = 0  # 1^2 + 2^2 + 3^2 + 4^2 +...+ 100^2
    sqOfSum = 0  # (1 + 2 + 3 + 4 +...+ 100)^2
    for i in range(1, 101):
        sumOfSq += i ** 2
        sqOfSum += i
    sqOfSum **= 2
    return [sqOfSum - sumOfSq, sqOfSum, sumOfSq]


def the10001stPrime():
    prime = [2, 3, 5, 7, 11, 13]
    for i in range(0, 9995):
        prime.append(nextprime(prime))
    return prime


def wtf():
    lst = []
    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    while (num > 0):
        lst.append(num % 10)
        num //= 10
    # while not(lst.count(0)==0):
    #    i = lst.index(0)
    #    if (i-10 < 0):
    #        del lst[0: i + 1]
    #    elif(i + 10 > len(lst)):
    #        del lst[i-10: len(lst)-1]
    #    else:
    #        del lst[i - 10: i + 10]
    # return [len(lst), lst]
    prod = []
    mul = 1
    print(lst)
    for j in range(0, len(lst) - 10):
        for f in range(j, j + 11):
            mul *= lst[f]
            print(lst[f])
        prod.append(mul)
        print(mul)
        mul = 1
    return max(prod)


def bigNumber():
    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    div = 10 ** 13
    list = []
    while (num > div - 1):
        list.append(num % div)
        num //= 10
    prod = 1
    prodLst = []
    for x in list:
        n = x
        for i in range(0, 13):
            prod *= n % 10
            n //= 10
        prodLst.append(prod)
        prod = 1
    return max(prodLst)


def pythagoTriplet():
    # a^2 + b^2 = c^2
    # a + b + c = 1000
    # a < b < c
    # c = 1000 - (a + b)
    for b in range(1, 999):
        for a in range(1, 1000 - b):
            if (a ** 2 + b ** 2 == (1000 - (a + b)) ** 2):
                return [a, b, 1000 - (a + b), a * b * (1000 - (a + b))]


def primeDigRep():
    prime = [2, 3, 5, 7, 11, 13]
    for i in range(0, 10001):
        prime.append(nextprime(prime))
    strPrime = []
    strPrime.extend(str(j) for j in prime)
    list = []
    group = []
    for n in range(1, 10):
        group.extend(x for x in strPrime if len(x) == n)
        list.append(group)
        group = []
        c = 2
    ans = []
    for g in list:
        for i in range(0, len(g) - 2):
            if len(g[i]) <= 4:
                break
            num = int(g[i])
            numPlus = int(g[i + 1])
            numPP = int(g[i + 2])
            dif = numPlus - num
            dif2 = numPP - numPlus
            dif3 = numPP - num
            if (has1NonZeroDig(dif) and has1NonZeroDig(dif2) and has1NonZeroDig(dif3) and sameLen(dif,
                                                                                                  dif3) and sameLen(dif,
                                                                                                                    dif2)):
                ans.append(num)
                c += 1
                print("c++")
            else:
                ans = []
                c = 2
                print("c = 0")
            if (c >= 8):
                ans.append(numPlus)
                ans.append(numPP)
                return ans
        c = 2
        ans = []


def sameLen(num1, num2):
    c = 0
    while (num1 > 0):
        c += 1
        num1 //= 10
    while (num2 > 0):
        c -= 1
        num2 //= 10
    if (c == 0):
        return True
    else:
        return False


def has1NonZeroDig(n):
    num = n
    while (num % 10 == 0):
        num //= 10
    dig = num % 10
    while (num > 0):
        if (num % 10 == dig):
            num //= 10
        else:
            return False
    if num == 0:
        return True


def primeList(length):
    list = [2, 3, 5, 7]
    i = 7
    while len(list) < length:
        if all(i % n != 0 for n in list):
            list.append(i)
        i += 1
    return list


def checkFamilyDif(dif1, dif2):
    i = 0
    while dif1 % 10 == 0:
        dif1 //= 10
        i += 1
    if i < 2:
        return False
    while dif2 % 10 == 0:
        dif2 //= 10
        i -= 1
    if (i != 0):
        return False
    n = dif1 % 10
    dif1 //= 10
    while (dif1 % 10 == n):
        dif1 //= 10
        i += 1
    n = dif2 % 10
    dif2 //= 10
    while (dif2 % 10 == n):
        dif2 //= 10
        i -= 1
    return (
            i == 0 and dif1 == 0 and dif2 == 0)


def primeFamily(num):
    prime = primeList(10001)
    # prime = [113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    c = 2
    print(prime)
    print(c)
    for i in range(0, len(prime) - num + 1):
        for j in range(0, num - 2):
            p1 = prime[i + j]
            p2 = prime[i + j + 1]
            p3 = prime[i + j + 2]
            if not bool(checkFamilyDif((p2 - p1), (p3 - p2))):
                break
            else:
                c += 1
                print("c :", c)
            if (c >= num):
                return prime[j: j + num - 1]
        c = 2
        print("c :", 0)


def primeFun():
    prime = primeList(10001)
    i = prime.index(56003)
    j = prime.index(56993)
    print(prime[i: j])
    print(i, "\t", j, "\t", j - i)


def boolFamilyDiff(prime1, prime2, prime3):
    dif1 = prime2 - prime1
    dif2 = prime3 - prime2
    i = 0
    while dif1 % 10 == 0:
        dif1 //= 10
        i += 1
    if i < 2:
        return False
    while dif2 % 10 == 0:
        dif2 //= 10
        i -= 1
    if (i != 0):
        return False
    n = dif1 % 10
    dif1 //= 10
    while (dif1 % 10 == n):
        dif1 //= 10
        i += 1
    n = dif2 % 10
    dif2 //= 10
    while (dif2 % 10 == n):
        dif2 //= 10
        i -= 1
    return (
            i == 0 and dif1 == 0 and dif2 == 0)


def boolFamilyDigits(prime1, prime2, prime3):
    prDig1 = []
    while (prime1 > 0):
        prDig1.append(prime1 % 10)
        prime1 //= 10
    prDig2 = []
    while (prime2 > 0):
        prDig2.append(prime2 % 10)
        prime2 //= 10
    prDig3 = []
    while (prime3 > 0):
        prDig3.append(prime3 % 10)
        prime3 //= 10
    if not (len(prDig1) == len(prDig3) and len(prDig2) == len(prDig3)):
        return False
    index = []
    for i in range(0, len(prDig1)):
        if not (prDig1[i] == prDig2[i] and prDig2[i] == prDig3[i] and prDig3[i] == prDig1[i]):
            index.append(i)
    if not all(index[j] - j == index[0] for j in range(1, len(index))):
        return False
    # if not all(prDig1[n] == prDig1[index[0]] for n in index):
    #     return False
    if not all(prDig2[n] == prDig2[index[0]] for n in index):
        return False
    if not all(prDig3[n] == prDig3[index[0]] for n in index):
        return False
    mid = prDig1[index[0]: index[-1] + 1]
    if all(dig == prDig1[index[0]] for dig in mid):
        return True


def bool1NonZeroDig(prime1, prime2):
    lstDig = []
    temp = prime1
    while (temp > 0):
        lstDig.append(temp % 10)
        temp //= 10
    # temp2 = prime2
    # lstDig2 = []
    # while (temp2 > 0):
    #     lstDig2.append(temp2 % 10)
    #     temp2 //= 10
    # if (len(lstDig) != len(lstDig2)):
    #     return False
    digDiff = []
    while (prime2 > 0):
        digDiff.append(prime2 % 10 - prime1 % 10)
        prime1 //= 10
        prime2 //= 10
    i = 0
    while (i < len(digDiff) and digDiff[i] == 0):
        i += 1
    if i >= len(digDiff):
        return False
    num = digDiff[i]
    if num == 0:
        return False
    index = []
    while (i < len(digDiff) and digDiff[i] == num):
        index.append(i)
        i += 1
    while (i < len(digDiff) and digDiff[i] == 0):
        i += 1
    if (i != len(digDiff)):
        return False
    if not all(index[j] - j == index[0] for j in range(1, len(index))):
        return False
    if all(lstDig[i] == lstDig[index[0]] for i in index):
        return True
    # mid = lstDig2[index[0]: index[-1] + 1]
    # if all(t == mid[0] for t in mid):
    #     return True


def bool1NonZeroDigDiffList(prime1, prime2):
    lstDig = []
    temp = prime1
    while (temp > 0):
        lstDig.append(temp % 10)
        temp //= 10
    # temp2 = prime2
    # lstDig2 = []
    # while (temp2 > 0):
    #     lstDig2.append(temp2 % 10)
    #     temp2 //= 10
    # if (len(lstDig) != len(lstDig2)):
    #     return False
    digDiff = []
    while (prime2 > 0):
        digDiff.append(prime2 % 10 - prime1 % 10)
        prime1 //= 10
        prime2 //= 10
    i = 0
    while (i < len(digDiff) and digDiff[i] == 0):
        i += 1
    if i >= len(digDiff):
        return [False, [0]]
    num = digDiff[i]
    if num == 0:
        return [False, [0]]
    index = []
    while (i < len(digDiff) and digDiff[i] == num):
        index.append(i)
        i += 1
    while (i < len(digDiff) and digDiff[i] == 0):
        i += 1
    if (i != len(digDiff)):
        return [False, [0]]
    if not all(index[j] - j == index[0] for j in range(1, len(index))):
        return [False, [0]]
    if all(lstDig[i] == lstDig[index[0]] for i in index):
        return [True, digDiff]
    else:
        return [False, [0]]
    # mid = lstDig2[index[0]: index[-1] + 1]
    # if all(t == mid[0] for t in mid):
    #     return True


def bool1NonZeroDifDig(prime1, prime2):
    n = prime2 - prime1
    num = n
    while (num % 10 == 0):
        num //= 10
    dig = num % 10
    while (num > 0):
        if (num % 10 == dig):
            num //= 10
        else:
            return False
    if num == 0:
        return True


def nextStrprime(prime):
    if (prime[0] == '2'):
        n = int(prime[-1])
    else:
        n = max(prime)
    bool = True
    # list = []
    while (bool):
        n += 1
        # list.extend(n % x != 0 for x in prime)
        if all(n % x != 0 for x in prime):
            return n


def primeDigRep2():
    prime = [2, 3, 5, 7, 11, 13]
    for i in range(0, 50001):
        prime.append(nextprime(prime))
    strPrime = []
    strPrime.extend(str(j) for j in prime)
    # print(strPrime)
    list = []
    group = []
    for n in range(4, 10):
        group.extend(x for x in strPrime if len(x) == n)
        list.append(group)
        group = []
    # print(list)
    prime = []
    for lst in list:
        group.extend(int(x) for x in lst)
        prime.append(group)
        group = []

    for lst in prime:

        for fir in range(0, len(lst) - 6):

            for sec in range(fir + 1, len(lst) - 5):
                if bool1NonZeroDig(lst[fir], lst[sec]):
                    c = 2
                    for i in range(sec + 1, len(lst) - 4):

                        # if (boolFamilyDif(lst[fir], lst[sec], lst[i])):
                        if boolFamilyDigits(lst[fir], lst[sec], lst[i]):
                            c += 1
                        if c >= 8:
                            print([lst[fir], lst[sec], lst[i]])
                            return lst[fir: i + 1]


def unitDigDiff(digDiff):
    unitDigDif = []
    for i in range(0, len(digDiff)):
        if digDiff[i] != 0:
            unitDigDif.append(1)
        else:
            unitDigDif.append(0)
    return unitDigDif


def digDiffPlusUnitToNum(digDiff, unitDigDiff):
    if digDiff == None or unitDigDiff == None:
        print("WTF?!?!? -       ", digDiff, " ", unitDigDiff)
    if (len(digDiff) == len(unitDigDiff)):
        for i in range(0, len(digDiff)):
            if (digDiff[i] + unitDigDiff[i] < 10):
                digDiff[i] += unitDigDiff[i]
            elif (digDiff[i] + unitDigDiff[i] == 10):
                digDiff[i] = 0
            else:
                digDiff[i] += unitDigDiff[i]
                digDiff[i] -= 10
        num = 0
        for dig in digDiff:
            num *= 10
            num += dig
        return num
    else:
        print("not working-   len(digDiff) != len(unitDigDiff)")
        return [0]


def digDiffList(prime1, prime2):
    digDiff = []
    while (prime2 > 0):
        digDiff.append(prime2 % 10 - prime1 % 10)
        prime1 //= 10
        prime2 //= 10
    return digDiff


def primeDigRep3():
    prime = [2, 3, 5, 7, 11, 13]
    for i in range(0, 80001):
        prime.append(nextprime(prime))
    lst = prime
    for fir in range(0, len(lst) - 2):
        for sec in range(fir + 1, len(lst) - 1):
            if len(str(lst[fir])) != len(str(lst[sec])):
                break
            if bool1NonZeroDig(lst[fir], lst[sec]):
                digDif = digDiffList(lst[fir], lst[sec])
                unitDigDif = unitDigDiff(digDif)
                c = 1
                for i in range(0, 10):
                    num = digDiffPlusUnitToNum(digDif, unitDigDif)
                    if num in lst:
                        c += 1
                if c >= 7:
                    return [lst[fir], lst[sec]]


# main
if __name__ == '__main__':
    print(primeDigRep3())
