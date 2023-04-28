import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class BOJ_15683 {
    // 1 : 한 방향, 2 : 양방향 (수평), 3 : 양방향 (수직), 4 : 세방향, 5 : 네방향
    // 번호를 매겨서 동서남북 방향으로 해보기
    static int[][] map;
    static ArrayList<CCTV> cctvs;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        cctvs = new ArrayList<>();
        map = new int[N][M];

        for (int r = 0; r < N; r++) {
            inputs = br.readLine().split( " ");
            for (int c = 0; c < M; c++) {
                map[r][c] = Integer.parseInt(inputs[c]);
                if(map[r][c] >= 1 && map[r][c] <= 5){
                    cctvs.add(new CCTV(r, c, map[r][c]));
                }
            }
        }

        // 순서 나누기
        sel = new int[cctvs.size()];
        comb(0);

        System.out.println(ans);
    }

    static int checkBlind(){
        int[][] cur = new int[map.length][map[0].length];
        for (int r = 0; r < map.length; r++) {
            cur[r] = Arrays.copyOfRange(map[r], 0, map[r].length);
        }

        for (int i = 0; i < cctvs.size(); i++) {
            CCTV cctv = cctvs.get(i);
            switch (cctv.type) {
                // 단방향
                case 1:
                    switch (sel[i]){
                        case 1:
                            upward(cctv, cur);
                            break;
                        case 2:
                            right(cur, cctv);
                            break;
                        case 3:
                            downward(cctv, cur);
                            break;
                        case 4:
                            left(cur, cctv);
                            break;
                    }
                    break;
                // 양방향 (수평)
                case 2:
                    switch (sel[i]){
                        case 1:
                        case 3:
                            upward(cctv, cur);
                            downward(cctv, cur);
                            break;
                        case 2:
                        case 4:
                            right(cur, cctv);
                            left(cur, cctv);
                            break;
                    }
                    break;
                // 양방향 (수직)
                case 3:
                    switch (sel[i]){
                        case 1:
                            upward(cctv, cur);
                            right(cur, cctv);
                            break;
                        case 2:
                            right(cur,cctv);
                            downward(cctv,cur);
                            break;
                        case 3:
                            downward(cctv, cur);
                            left(cur, cctv);
                            break;
                        case 4:
                            left(cur, cctv);
                            upward(cctv, cur);
                            break;
                    }
                    break;
                case 4:
                    switch (sel[i]){
                        case 1:
                            upward(cctv, cur);
                            right(cur, cctv);
                            left(cur, cctv);
                            break;
                        case 2:
                            right(cur,cctv);
                            downward(cctv,cur);
                            upward(cctv, cur);
                            break;
                        case 3:
                            downward(cctv, cur);
                            left(cur, cctv);
                            right(cur, cctv);
                            break;
                        case 4:
                            left(cur, cctv);
                            upward(cctv, cur);
                            downward(cctv, cur);
                            break;
                    }
                    break;
                case 5:
                    upward(cctv, cur);
                    right(cur, cctv);
                    left(cur, cctv);
                    downward(cctv, cur);
                    break;
            }
        }

        // 빈 칸 체크
        int count = 0;
        for (int r = 0; r < cur.length; r++) {
            for (int c = 0; c < cur[0].length; c++) {
                if(cur[r][c] == 0){
                    count++;
                }
            }
        }

        return count;
    }

    private static void left(int[][] cur, CCTV cctv) {
        for (int c = cctv.c; c >= 0; c--) {
            if(cur[cctv.r][c] == 6){
                break;
            }else{
                cur[cctv.r][c] = -1;
            }
        }
    }

    private static void downward(CCTV cctv, int[][] cur) {
        for (int r = cctv.r; r < cur.length; r++) {
            if(cur[r][cctv.c] == 6){
                break;
            }else{
                cur[r][cctv.c] = -1;
            }
        }
    }

    private static void right(int[][] cur, CCTV cctv) {
        for (int c = cctv.c; c < cur[cctv.r].length; c++) {
            if(cur[cctv.r][c] == 6){
                break;
            }else{
                cur[cctv.r][c] = -1;
            }
        }
    }

    private static void upward(CCTV cctv, int[][] cur) {
        for (int r = cctv.r; r >= 0; r--) {
            if(cur[r][cctv.c] == 6){
                break;
            }else{
                cur[r][cctv.c] = -1;
            }
        }
    }

    // 1 ~ 4 순서 중 하나를 골라서 선택하기 (타입 고려 X)
    static int[] sel;
    static int[] arr = {1, 2, 3, 4};
    static int ans = Integer.MAX_VALUE;
    static void comb(int idx){
        if(idx == sel.length){
            // 각 방향별 사각지대 찾기
            ans = Math.min(ans, checkBlind());
            return;
        }

        for (int i = 0; i < arr.length; i++) {
            sel[idx] = arr[i];
            comb(idx+1);
        }
    }
    
    static class CCTV{
        int r, c, type;

        public CCTV(int r, int c, int type) {
            this.r = r;
            this.c = c;
            this.type = type;
        }
    }
}
