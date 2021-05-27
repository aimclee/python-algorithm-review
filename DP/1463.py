# 입력
x=int(input())

# memoization
d = [0]*1000001


for i in range(2, x+1):
    # 먼저 1을 빼는 경우 나오는 경우의 수 저장
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1) # min : 횟수의 최솟값을 구하기 위함.

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    

# 연산 횟수의 최솟값 출력
print(d[x])