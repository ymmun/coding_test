# 출저: https://www.acmicpc.net/problem/14929

# 풀이 : 해당 식을 전개하면
#     x1x2 + x1x3 + x1x4 + ... + x1xn
#            x2x3 + x2x4 + ... + x2xn
#                 + x3x4 + ... + x3xn
# = x1(x2 + x3 + x4 + ... + xn) + x2(x3 + x4 + ... + xn) + ... + xn-1(xn)
# 위의 식을 코드로 풀면 된다.

def question() -> int:
    n = int(input())
    x_list = list(map(int, input().split()))

    temp = [x_list[0]]
    for i in range(1, n):
        temp.append(temp[i-1] + x_list[i])  # [x1, x1+x2, x1+x2+x3 ....]

    answer = 0
    for i in range(len(x_list)):
        answer += x_list[i] * (temp[n-1] - temp[i])  # x1*[x2+x3+x4] + x2*[x3+x4] + ....

    return answer


if __name__ == '__main__':
    question()
