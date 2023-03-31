import sys
sys.stdin = open("이태엽\swea_16003_화면캡쳐\input.txt", "r")


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     files = []
#     answer = ""
#     for i in range(1, int(N) + 1):
#         file = str(i) + ".png"
#         files.append(file)
#     sorted_files = sorted(files)
#     if N > 50:
#         print("#{}".format(tc),end=' ')
#         for i in range(50):
#             print("{}".format(sorted_files[i]),end=' ')
#     else:
#         print("#{}".format(tc),end=' ')
#         for i in sorted_files:
#             print("{}".format(i),end=' ')
#     print()

def getNumList(maxNum):
	num = 1
	for i in range(50):
        # 기록하면서 개행없이 나아가자
		print(f"{num}.png", end=' ')
        # num의 맨 왼쪽 첫자리 숫자 * 10이 아직 최대수 이하라면
		if(num * 10 <= maxNum):
			num *= 10
        
		elif(num + 1 <= maxNum):
            # num의 맨 오른쪽 자리 숫자가 9라면
			if num % 10 == 9:
				num = num // 10
                # num을 10으로 나눈 몪이 0, 즉 elif문 시작할 때 시점의 num이 9라면 그대로 종료된다.
                # 이 break문은 50 이하에서 끝나는 상황에 maxNum의 맨 오른쪽 자리의 숫자가 9인 상황을 위해 존재
				if(num == 0):
					break
			num += 1
		else:
			num //= 10
			if(num == 0):
				break
			num += 1
T = int(input())
for t in range(1, T + 1):
	N = int(input())
	print(f"#{t}", end=' ')
	getNumList(N)
	print()