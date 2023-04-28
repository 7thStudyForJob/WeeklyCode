import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

// 어떤 자료구조?

public class BOJ_15684 {
    static int N, M, H, Ans = Integer.MAX_VALUE;
    static boolean[][] ladder;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        H = Integer.parseInt(inputs[2]);

        // 0은 없음, 1은 왼쪽, 2는 오른쪽
        ladder = new boolean[H+1][N+1];


        for (int i = 0; i < M; i++) {
            inputs = br.readLine().split(" ");
            int height = Integer.parseInt(inputs[0]);
            int start = Integer.parseInt(inputs[1]);
            int end = start + 1;

            // 양방향
            ladder[height][start] = true;
        }

        // 사다리 개수 놓기
        DFS(1, 0);

        System.out.println(Ans == Integer.MAX_VALUE ? -1 : Ans);
    }

    static void DFS(int row, int count){
        // 3개 이상이면 탈출
        if(count > 3){
            return;
        }else{
            if(check()){
                Ans = Math.min(Ans, count);
                return;
            }
        }

        for (int c = 1; c < N; c++) {
            for (int r = row; r <= H; r++) {
                // 사다리 놔 보기
                // 양 옆에 인근 X
                if(ladder[r][c] || ladder[r][c-1] || ladder[r][c+1]) continue;

                ladder[r][c] = true;
                DFS(r, count + 1);
                // 사다리 빼기
                ladder[r][c] = false;

            }
        }

    }

    // 사다리 타기 시뮬레이션

    static boolean check(){
        for (int c = 1; c <= N; c++) {
            int state = c;
            for (int r = 1; r <= H; r++) {
                if(ladder[r][state]){
                    state++;
                }else if(ladder[r][state-1]){
                    state--;
                }
            }

            if(state != c){
                return false;
            }
        }
        return true;
    }
}
