import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_12100 {
    static int N;
    static int[][] map;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        for (int r = 0; r < N; r++) {
            String[] inputs = br.readLine().split(" ");
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(inputs[c]);
            }
        }

        DFS(0);

        System.out.println(ans);
    }

    static int ans = 0;

    static void DFS(int cnt){
        if(cnt == 5){
            int cur = 0;
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    cur = Math.max(cur, map[r][c]);
                }
            }
            ans = Math.max(ans, cur);
            return;
        }

        // 백트래킹 해보기
        int origin[][] = new int[N][N];
        for(int i = 0; i < N; i++)
            origin[i] = map[i].clone();

        for(int i = 1; i <= 4; i++) {
            move(i);
            DFS(cnt+1);
            // 백트래킹
            for(int a = 0; a < N; a++)
                map[a] = origin[a].clone();
        }
    }
    static void move(int dir){
        switch (dir){
            case 1:
                upward(new boolean[N][N]);
                break;
            case 2:
                downward(new boolean[N][N]);
                break;
            case 3:
                right(new boolean[N][N]);
                break;
            case 4:
                left(new boolean[N][N]);
                break;
        }
    }

    static void upward(boolean[][] v){
        // 위로 이동 -> 먼저 합치고 서로 올리기
        for (int c = 0; c < N; c++) {
            // 먼저 합치기
            for (int r = 1; r < N; r++) {
                if(map[r][c] != 0) {
                    int nr = r - 1;
                    while (nr >= 0 && map[nr][c] == 0) {
                        nr--;
                    }
                    // 위에 같은 숫자 있음
                    if (nr >= 0 && !v[nr][c] && map[nr][c] == map[r][c]) {
                        map[nr][c] *= 2;
                        map[r][c] = 0;
                        v[nr][c] = true;
                    }
                }
            }

            // 위로 올리기
            for (int r = 1; r < N; r++) {
                if(map[r][c] != 0) {
                    int nr = r - 1;
                    while (nr >= 0 && map[nr][c] == 0) {
                        nr--;
                    }
                    // 숫자 올림
                    if(nr == -1){
                       map[0][c] = map[r][c];
                       map[r][c] = 0;
                    }else if(map[nr + 1][c] == 0){
                        map[nr+1][c] = map[r][c];
                        map[r][c] = 0;
                    }
                }
            }
        }
    }

    static void downward(boolean[][] v){
        // 아래로 이동 -> 먼저 합치고 서로 올리기
        for (int c = 0; c < N; c++) {
            // 먼저 합치기
            for (int r = N - 2; r >= 0; r--) {
                if(map[r][c] != 0) {
                    int nr = r + 1;
                    while (nr < N && map[nr][c] == 0) {
                        nr++;
                    }
                    // 위에 같은 숫자 있음
                    if (nr < N && !v[nr][c] && map[nr][c] == map[r][c]) {
                        map[nr][c] *= 2;
                        map[r][c] = 0;
                        v[nr][c] = true;
                    }
                }
            }

            // 아래로 내리기
            for (int r = N - 2; r >= 0; r--) {
                if(map[r][c] != 0) {
                    int nr = r + 1;
                    while (nr < N && map[nr][c] == 0) {
                        nr++;
                    }
                    // 숫자 올림
                    if(nr == N){
                        map[N-1][c] = map[r][c];
                        map[r][c] = 0;
                    }else if(map[nr - 1][c] == 0){
                        map[nr-1][c] = map[r][c];
                        map[r][c] = 0;
                    }
                }
            }
        }
    }

    static void right(boolean[][] v){
        // 오른쪽으로 이동 -> 먼저 합치고 서로 올리기
        for (int r = 0; r < N; r++) {
            // 먼저 합치기
            for (int c = N - 2; c >= 0; c--) {
                if(map[r][c] != 0) {
                    int nc = c + 1;
                    while (nc < N && map[r][nc] == 0) {
                        nc++;
                    }
                    // 같은 숫자 있음
                    if (nc < N && !v[r][nc] && map[r][nc] == map[r][c]) {
                        map[r][nc] *= 2;
                        map[r][c] = 0;
                        v[r][nc] = true;
                    }
                }
            }

            // 오른쪽으로 옮기기
            for (int c = N - 2; c >= 0; c--) {
                if(map[r][c] != 0) {
                    int nc = c + 1;
                    while (nc < N && map[r][nc] == 0) {
                        nc++;
                    }
                    // 숫자 올림
                    if(nc == N){
                        map[r][N - 1] = map[r][c];
                        map[r][c] = 0;
                    }else if(map[r][nc - 1] == 0){
                        map[r][nc - 1] = map[r][c];
                        map[r][c] = 0;
                    }
                }
            }
        }
    }

    static void left(boolean[][] v){
        // 왼쪽으로 이동 -> 먼저 합치고 서로 올리기
        for (int r = 0; r < N; r++) {
            // 먼저 합치기
            for (int c = 1; c < N; c++) {
                if(map[r][c] != 0) {
                    int nc = c - 1;
                    while (nc >= 0 && map[r][nc] == 0) {
                        nc--;
                    }
                    // 같은 숫자 있음
                    if (nc >= 0 && !v[r][nc] && map[r][nc] == map[r][c]) {
                        map[r][nc] *= 2;
                        map[r][c] = 0;
                        v[r][nc] = true;
                    }
                }
            }

            // 왼쪽으로 옮기기
            for (int c = 1; c < N; c++) {
                if(map[r][c] != 0) {
                    int nc = c - 1;
                    while (nc >= 0 && map[r][nc] == 0) {
                        nc--;
                    }
                    // 숫자 올림
                    if(nc == -1){
                        map[r][0] = map[r][c];
                        map[r][c] = 0;
                    }else if(map[r][nc + 1] == 0){
                        map[r][nc + 1] = map[r][c];
                        map[r][c] = 0;
                    }
                }
            }
        }
    }
}

