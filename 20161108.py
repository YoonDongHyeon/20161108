def max_number(n):
    x=n//10
    if x>=10:
        x=max_number(x)
    return x

def factorial(n):
    if n == 0:
        return 1
    k = n *factorial(n-1)
    return k
# 재귀적 용법

print(factorial(4))

# 퀵 소트(quick sort)
# 숫자 배열이 있으면 첫번째 값을 PIVOT으로 잡고 그거보다 작은거는 왼쪽으로 큰것은 오른쪽으로
#  마지막에 len값이 0<= <=1이면 종료조건

def quick_sort(n):
    if len(n) <=1:
        return n
    left = []
    right = []
    pivot = []
    pivot.append(n[0])
    for i in range(1,len(n)):
        if(pivot[0] > n[i]):
            left.append(n[i])
        elif(pivot[0] == n[i]):
            pivot.append(n[i])
        elif(pivot[0] < n[i]):
            right.append(n[i])

    return quick_sort(left) + pivot + quick_sort(right)
    # return left
    # return right
#< 교수님꺼 >
def quick_sort2(x):
    if len(x) <=1:
        return x

    pivot = [x[0]]
    left = []
    right =[]

    for i in x[1:]:
        if i < pivot[0]:
            left.append(i)
        elif i > pivot[0]:
            right.append(i)
        else:
            pivot.append(i)

    return quick_sort2(left) + pivot + quick_sort2(right)

n=[7,9,6,5,3,4,2]
print(quick_sort(n))
print(quick_sort2(n))