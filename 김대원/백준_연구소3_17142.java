import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_17142 {
    static int N, M, empty;
    static int[][] map;
    static boolean[][] v;
    static int[] selected;
    static ArrayList<Point> virus;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        map = new int[N][N];
        virus = new ArrayList<>();
        selected = new int[M];

        for (int r = 0; r < N; r++) {
            inputs = br.readLine().split(" ");
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(inputs[c]);
                if(map[r][c] == 2){
                    virus.add(new Point(r, c, 0));
                }
                if(map[r][c] == 0){
                    empty++;
                }
            }
        }
        if(empty == 0){
            System.out.println(0);
            return;
        }

        recursive(0, 0);

        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    static int[][] dir = {{-1, 0},{0, 1},{1, 0},{0, -1}};
    static int spreadVirus(){
        Queue<Point> q = new LinkedList<>();
        v = new boolean[N][N];
        int count = empty;

        for (int sel: selected) {
            Point p = virus.get(sel);
            q.offer(p);
            v[p.r][p.c] = true;
        }

        while (!q.isEmpty()){
            Point p = q.poll();

            for (int d = 0; d < 4; d++) {
                int nr = p.r + dir[d][0];
                int nc = p.c + dir[d][1];

                if(nr >= 0 && nr < N && nc >= 0 && nc < N && !v[nr][nc] && map[nr][nc] != 1){
                    q.offer(new Point(nr, nc, p.time+1));
                    v[nr][nc] = true;
                    if(map[nr][nc] == 0) {
                        count--;
                    }
                    if(count == 0){
                        return p.time+1;
                    }
                }
            }
        }
        return Integer.MAX_VALUE;
    }

    static int answer = Integer.MAX_VALUE;
    static void recursive(int idx, int k){
        if(idx == M){
            answer = Math.min(answer, spreadVirus());
            return;
        }

        if(k == virus.size()){
            return;
        }

        selected[idx] = k;
        recursive(idx+1, k+1);
        recursive(idx, k+1);
    }

    static class Point{
        int r, c, time;

        public Point(int r, int c, int time) {
            this.r = r;
            this.c = c;
            this.time = time;
        }

        @Override
        public String toString() {
            return "Point{" +
                    "r=" + r +
                    ", c=" + c +
                    ", time=" + time +
                    '}';
        }
    }
}
