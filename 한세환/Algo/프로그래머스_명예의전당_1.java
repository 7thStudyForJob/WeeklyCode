package programmers;

import java.security.Key;
import java.util.*;

/*
 * 문제 정보 : 프로그래머스, 명예의 전당(1) ( https://school.programmers.co.kr/learn/courses/30/lessons/138477 )
 * 풀이 : 1번째 풀이는 리스트를 활용하여 k의 사이즈 만큼 값을 입력 받고 이를
 *       정렬하여 최소값과 이 다음 입력값을 비교하여 answer 리스트에 넣는 방식으로 하였습니다.
 *       2번째 풀이는 앞서 활용했던 리스트와 정렬을 우선순위큐로 대신하여 k의 사이즈가 넘어가면 첫번째 값을 빼는 형식으로 구현하였습니다. (외부 참조)
 *
 */

public class Solution_명예의전당_1 {

    // 1번째 풀이
    public static List<Integer> solution1(int k, int[] score) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> list  = new ArrayList<>();
        int temp = Integer.MAX_VALUE;
        for (int i = 0; i < score.length; i++) {
            if(list.size()<k){
                list.add(score[i]);
                Collections.sort(list);
                temp = Math.min(temp,list.get(0));
            }
            else{
                if(score[i]>list.get(0)){
                    list.remove(0);
                    list.add(score[i]);
                }
                Collections.sort(list);
                temp = list.get(0);
            }
            answer.add(temp);
        }
        return answer;
    }

    public int[] solution2(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int temp = 0;

        for(int i=0;i<score.length;i++){
            pq.add(score[i]);

            if(pq.size()>k){
                pq.poll();
            }
            answer[i] = pq.peek();

        }

        return answer;
    }

    public static void main(String[] args) {

//        List<Integer> a = solution(3, new int[]{10, 100, 20, 150, 1, 100, 200});
//
//        for(int i : a){
//            System.out.println(i);
//        }


    }
}
