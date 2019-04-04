def fact(n):
    if n == 1:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res = i * res
        print(res)
fact(5)

def fib():
    x = 1
    y = 1
    i = 0
    res = 0
    while True:
        if res > 1000000000000:
            break
        res = x + y
        x = y
        y = res
        #print(res , sep=",")
fib()



def nod(a, b):
    #return a if b == 0 else nod(b, a%b) #решение рекурсией
    #"""   нахожнение НОД нормального человека """
   while a != 0 and  b != 0:
       if a > b:
           a = a - b
       else:
           b = b - a
   print(a + b)
nod(30 , 18)

def nod_test(a,b):
    return a if b == 0 else nod_test(b, a % b)

print(nod_test(50,36))


def list_ex(seq):
    flat_lis = []
    for i in seq:
        if isinstance(i,tuple) or isinstance(i,list):
            flat_lis.extend(list_ex(i))
        else:
            flat_lis.append(i)
    return flat_lis

seq =[1,2,[2,4,[5,7],8,[5],9]]
print(list_ex(seq))
print(seq)

def flat_l_without_rec(seq):
    while seq:
        tmp = seq.pop()

        if isinstance(i,tuple) or isinstance(i,list):
            yield
        else:
            flat_l.append(i)