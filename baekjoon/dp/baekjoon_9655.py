# 출저 : https://www.acmicpc.net/problem/9655

# 풀이: 홀수면 상근이가 승리, 짝수면 창영이가 승리

def question() -> None:
    n = int(input())

    if n % 2 == 0:
        print('CY')
        return
    print('SK')
    return


if __name__ == '__main__':
    question()
