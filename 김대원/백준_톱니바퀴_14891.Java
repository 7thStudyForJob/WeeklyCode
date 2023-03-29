import java.io.BufferedReader;
import java.io.InputStreamReader;

// 8방향으로 있는 4개의 톱니바퀴
// 시계 or 반시계 회전
// 하나를 선택하여 회전할 때, 맞닿은 톱니의 극이 다르면 반대로 회전한다.
// 마지막에 각 톱니바퀴의 12시 방향이 S극이면 점수 획득

// 1. 시계를 돌린다
// 2. 양 옆의 톱니를 체크하고 돌린다
// 3.
public class BOJ_14891 {
    static int[][] magnets;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        magnets = new int[4][8];
        for (int i = 0; i < 4; i++) {
            String input = br.readLine();
            for (int c = 0; c < 8; c++) {
                magnets[i][c] = input.charAt(c) - '0';
            }
        }
        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            String[] raw = br.readLine().split(" ");
            int idx = Integer.parseInt(raw[0]) - 1;
            int rDir = Integer.parseInt(raw[1]);
            operation(idx, rDir, new boolean[4]);
        }
        // 점수 계산 : 0 : N, 1 : S
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            if(magnets[i][0] == 1){
                sum += Math.pow(2, i);
            }
        }

        System.out.println(sum);
    }
    static void operation(int idx, int rotateDir, boolean[] v) {
        int beforeR = magnets[idx][2];
        int beforeL = magnets[idx][6];
        rotate(idx, rotateDir);
        v[idx] = true;
        if (idx >= 1 && !v[idx-1]){
            if(beforeL != magnets[idx-1][2]){
                operation(idx-1, rotateDir * -1, v);
            }
        }
        if (idx < 3 && !v[idx+1]){
            if(beforeR != magnets[idx+1][6]){
                operation(idx+1, rotateDir * -1, v);
            }
        }
    }

    static void rotate(int idx, int rotateDir){
        // 시계 방향
        if(rotateDir == 1){
            int temp =  magnets[idx][7];
            for (int i = 7; i > 0; i--) {
                magnets[idx][i] = magnets[idx][i-1];
            }
            magnets[idx][0] = temp;
        }
        // 반 시계방향
        else{
            int temp = magnets[idx][0];
            for (int i = 0; i < 7; i++) {
                magnets[idx][i] = magnets[idx][i+1];
            }
            magnets[idx][7] = temp;
        }
    }
}
