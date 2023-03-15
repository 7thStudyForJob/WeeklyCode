package programmers;

import java.util.Arrays;

public class Solution_덧칠하기 {

    public static int solution(int n, int m, int[] section) {
        int answer = 0;
        boolean[] paint = new boolean[n];

        Arrays.fill(paint, true);

        for (int i : section) {
            paint[i-1] = false;
        }

        for(int i = 0 ; i<n;i++){
            if(!paint[i]){
                for(int j=i;j<i+m;j++){
                    if(j>=n)
                        break;
                    paint[j]=true;
                }
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(8, 4, new int[]{2, 3, 6}));
        System.out.println(solution(5, 4, new int[]{1,3}));
        System.out.println(solution(4, 1, new int[]{1,2,3,4}));


    }
}
