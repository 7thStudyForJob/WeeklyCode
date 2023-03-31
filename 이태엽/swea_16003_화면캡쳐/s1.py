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
		print(f"{num}.png", end=' ')
		if(num * 10 <= maxNum):
			num *= 10
		elif(num + 1 <= maxNum):
			if num % 10 == 9:
				num = num // 10
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