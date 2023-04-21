S, P = map(int, input().split())
string = list(input())
rule = list(map(int, input().split()))

# 각 글자별 개수를 기록할 배열
now = [0, 0, 0, 0]

# 문자를 기록 배열의 인덱스로 바꿔줄 딕셔너리
translate = {"A": 0, "C": 1, "G": 2, "T": 3}

# 첫 문자열 비밀번호를 보고 개수를 미리 세기
for i in range(P):
    now[translate[string[i]]] += 1

# 첫번째 비밀번호가 조건에 맞는지 확인
for j in range(4):
    if now[j] < rule[j]:
        cnt = 0
        break
else:
    cnt = 1

start = 0
# 한칸씩 이동하면서 카운트
while start + P < S:
    # 문자열에서 첫번째 글자를 빼주고
    prev = translate[string[start]]
    now[prev] -= 1

    # 마지막 문자에서 한칸을 더해 추가해주기
    next = translate[string[start + P]]
    now[next] += 1

    # now 배열을 갱신했으므로 조건에 맞는지 다시 확인
    for d in range(4):
        if now[d] < rule[d]:
            break
    else:
        cnt += 1

    # 한칸씩 이동 후 다시 체크
    start += 1

print(cnt)