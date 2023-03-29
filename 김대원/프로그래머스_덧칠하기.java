package level2;
// 투포인터를 써볼까?

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 덧칠하기 {
    static int n = 8;
    static int m = 4;
    static int[] section = {1,3,6,7};
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        for (int s: section) {
            q.offer(s);
        }

        //가장 작은 것부터 꺼내서 색칠하기
        int cnt = 0;
        while(!q.isEmpty()) {
            int start = q.peek();
            int end = start + m - 1;

            while (!q.isEmpty() && end >= q.peek()) {
                q.poll();
            }

            cnt++;
        }
    }
}
