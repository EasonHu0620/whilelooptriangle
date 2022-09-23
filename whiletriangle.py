#左直角三角形
n=eval(input("請輸入數字:"))
i=1
while i<=n:
    print("@"*i)
    i += 1

#倒左直角三角形
n = eval(input("請輸入數字:"))
i=0
while i<= n:
    print("@"*(n-i))
    i += 1

#右直角三角形
n = eval(input("請輸入數字:"))
i=1
while i<= n:
    print(" "*(n-i)+"@"*i)
    i +=1

#倒右直角三角形
n = eval(input("請輸入數字:"))
i=0
while i<= n:
    print(" "*i+"@"*(n-i))
    i +=1

#正等腰三角
n = eval(input("請輸入數字:"))
i=1
while i<= n:
    print(" "*(n-i)+"@"*(2*i-1))
    i +=1

#倒等腰三角
n = eval(input("請輸入數字:"))
i=n
while i>= 0:
    print(" "*(n-i)+"@"*(2*i-1))
    i -=1