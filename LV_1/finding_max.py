# 리스트에서 큰 수와 그 수의  index number 찾기
# 반대는   if a[i] < max_v: (방향 바꿔주기)

def max_find(a):
    n = len(a)
    max_v = a[0]
    max_idx = 0
    
    for i in range(n):
        if a[i] > max_v:
            max_v = a[i]
            max_idx = i
    return max_v, max_idx