import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_13549 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        // BFS
        Queue<Integer> q = new LinkedList<>();
        int[] v = new int[100001];
        q.offer(N);
        Arrays.fill(v, -1);
        v[N] = 0;

        while(!q.isEmpty()){
            int c = q.poll();

            if(c == K){
                break;
            }

            //0초부터
            if(c*2 <= 100000 && v[c*2] == -1){
                q.offer(c*2);
                v[c*2] = v[c];
            }

            if(c-1 >= 0 && v[c-1] == -1){
                q.offer(c-1);
                v[c-1] = v[c] + 1;
            }

            if(c+1 <= 100000 && v[c+1] == -1){
                q.offer(c+1);
                v[c+1] = v[c] + 1;
            }
        }

        System.out.println(v[K]);
    }
}
