# 출저: https://programmers.co.kr/learn/courses/30/lessons/60057

# 풀이: 하나씩 해보는 수밖에 없다.
# 첫번째 for 문에서 길이는 절반까지 해도 된다. (절반 이상은 같은 문자가 나올수 없으므로 줄일 수 없다)

def solution(s) -> int:
    half_length = len(s)//2 + 1
    answer = len(s)

    for i in range(1, half_length):
        count = 1
        tmp = ''
        letter = s[:i]

        for j in range(i, len(s), i):
            if letter == s[j:j+i]:
                count += 1
            else:
                if count > 1:
                    tmp += str(count)
                tmp += letter
                letter = s[j:j+i]
                count = 1
        if count > 1:
            tmp += str(count)
        tmp += letter
        answer = min(answer, len(tmp))

    return answer


if __name__ == '__main__':
    solution('aabbaccc')
