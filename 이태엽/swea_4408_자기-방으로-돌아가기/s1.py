import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
  
  N = int(input())
  students_array = [list(map(int, input().split())) for _ in range(N)]
  answer = 0
  room_array = [0]*401

  # 항상 작은 숫자 방에서 큰 숫자 방으로만 움직이는 게 아니라는 걸 몰라서 자꾸 오답을 냈습니다
  # 또, 방 배열 구조를 1차원행렬로 이해해서 마지막 TC에서 오답이 났습니다.
  # 홀수행, 짝수행으로 이루어진 2차원 구조이기에... 1~5 이동이면 6번 방에 들어가야 하는 학생도 한 타임 밀리게 되죠
  # 이 문제를 해결하기 위해서는 1과 2가 같은 방, 3과 4가 같은 방, 5와 6이 같은 방으로 취급되어야 한다고 생각했습니다.
  for student in students_array:
    
    if student[0] <= student[1]:
      start = (student[0]-1)//2
      end = (student[1]-1)//2
      
      for i in range(start, end+1):
        room_array[i]+=1
        
    else:
      start = (student[1]-1)//2
      end = (student[0]-1)//2
      
      for i in range(start, end+1):
        room_array[i]+=1
        
  answer = max(room_array)  
  
  print('#{} {}'.format(test_case, answer))