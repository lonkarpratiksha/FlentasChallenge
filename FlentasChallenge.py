t=int(input())
for i in range(t):
    str1=input()
    str2=input()
    a = sorted(str1)
    b = sorted(str2)
    for i in range(0, len(a)):
        if a[i] in b:
            result="YES"
            b.remove(a[i])
        else:
            result="NO"
            break
    print(result)