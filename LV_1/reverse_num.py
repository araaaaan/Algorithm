#reverse 사용하지 않고 역순으로 숫자 뽑기
# 1
def reverse(num): 
    first = end = 0
    
    while num >= 1:
        first = num % 10
        end   = end * 10 + first
        num   = num // 10
    return end

#2
def reverse(num2): 
    reverse_n = ""
    num2      = str(num2)
    
    for i in num2: 
        reverse_n = i + reverse_n
    return reverse_n
