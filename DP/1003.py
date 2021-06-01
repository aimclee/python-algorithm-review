# DP로 풀 때 memoization을 처음부터 만들 수도 있지만 append를 통해 계속 memo할 수도 있다.

T = int(input())
 
zero = [1,0,1]
one = [0,1,1]
 
def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))
 
for i in range(T):
    k = int(input())
    cal(k)


# 출처: https://doorbw.tistory.com/58 [Tigercow.Door]



'''
T = int(input())

dp_zero = [0] * 41
dp_one = [0] * 41

dp_zero[0] = 1
dp_one[0] = 1

def fibo(a):
    if a == 0:
        return dp_zero[0]
    elif a == 1:
        return dp_one[0] 
    else:
        return fibo(a-1) + fibo(a-2)


for i in range(T):
    a = int(input())
    print(fibo(a)) # 0과 1이 출력되는 횟수의 합이 나타난다.
    # print(, end=' ')
'''