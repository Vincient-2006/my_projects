l = list(map(int, input("enter building length seperated by commas: ").split(",")))
b = list(map(int, input("enter breadth of each building separated by commas: ").split(",")))
d = len(l)
k = 0
a = 0
n = 0
l_max = l[0]
i_max = 0

for i in range(d-1):
    if l_max < l[i+1]:
        l_max = l[i+1]
        i_max = i+1

if l[0] == l_max:
    for i in range(1, i_max):
        a = a + (l_max - l[i])*b[i]
else:
    while k < (i_max):
        m = 0
        n = l[k]
        for i in range(k, (i_max-1), 1):
            if n > l[i+1]:
                m = m + 1
            else:
                break

        for i in range(k+1, k+m+1):
            a = a + (n - l[i])*b[i]

        if m > 0:
            k = k+m+1
        else:
            k = k + 1

k = - 1
i_max = i_max - d

if l_max == l[d-1]:
    for i in range(-2, i_max, -1):
        a = a + (l_max - l[i])*b[i]
else:
    while k > (i_max):
        m = 0
        n = l[k]
        for i in range(k, (i_max+1), -1):
            if n > l[i-1]:
                m = m + 1
            else:
                break

        for i in range(k-1, k-m-1, -1):
            a = a + (n - l[i])*b[i]

        if m > 0:
            k = k-m-1
        else:
            k = k - 1

print("Area = ", a)