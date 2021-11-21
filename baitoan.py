

a = [5, 8, 4, 1, 2, 3, 9]
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[i] < a[j]:
            tam = a[i]
            a[i] = a[j]
            a[j] = tam

# giảm dần
a = [5, 8, 4, 1, 2, 3, 9]
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[i] < a[j]:
            tam = a[i]
            a[i] = a[j]
            a[j] = tam

