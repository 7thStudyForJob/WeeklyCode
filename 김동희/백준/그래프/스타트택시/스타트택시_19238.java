import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 스타트택시_19238 {

    static class Pos {
        int r;
        int c;

        public Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static int n, m, f;
    static int[][] arr;
    static int[][] visited;
    static Pos taxi;
    static List<Pos> people;
    static List<Pos> dest;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        f = Integer.parseInt(st.nextToken());
        arr = new int[n+1][n+1];
        people = new ArrayList<>();
        dest = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        taxi = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int sr = Integer.parseInt(st.nextToken());
            int sc = Integer.parseInt(st.nextToken());
            int er = Integer.parseInt(st.nextToken());
            int ec = Integer.parseInt(st.nextToken());
            people.add(new Pos(sr, sc));
            dest.add(new Pos(er, ec));
        }

        for (int i = 0; i < m; i++) {
            // 1. bfs로 이동 거리 찍어두고
            visited = new int[n + 1][n + 1];
            bfs(taxi.r, taxi.c);
            // 2. 가장 적은(거리, 행, 렬) 수 선택해서 초기점 바꿔준다.
            int minv = Integer.MAX_VALUE;
            int nr = 0, nc = 0, idx = -1;
            for (int j = 0; j < people.size(); j++) {
                Pos person = people.get(j);
                int r = person.r;
                int c = person.c;
                if (visited[r][c] < minv) {
                    nr = r;
                    nc = c;
                    idx = j;
                    minv = visited[r][c];
                } else if (visited[r][c] == minv) {
                    if (r < nr) {
                        nr = r;
                        nc = c;
                        idx = j;
                    } else if (nr == r && c < nc) {
                        nr = r;
                        nc = c;
                        idx = j;
                    }
                }
            }
            people.remove(idx);
            taxi.r = nr;
            taxi.c = nc;

            f -= (visited[nr][nc] - 1);
            // 못가게 되었을 때 - 1 해주고 넘어간다.
            if (visited[nr][nc] == 0) {
                f = -1;
                break;
            }
            // 연료 검사
            if (f <= 0) {
                break;
            }

            // 목적지 까지 또 찍어
            visited = new int[n + 1][n + 1];
            bfs(taxi.r, taxi.c);

            // 목적지로 이동
            Pos destination = dest.get(idx);
            int cr = destination.r;
            int cc = destination.c;
            if (visited[cr][cc] == 0) {
                f = -1;
                break;
            }
            taxi.r = cr;
            taxi.c = cc;
            dest.remove(idx);
            f -= (visited[cr][cc] - 1);

            if (f < 0) {
                break;
            }
            f += ((visited[cr][cc] - 1) * 2);
        }
        if (f <= 0) {
            System.out.println(-1);
        } else {
            System.out.println(f);
        }
    }

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    private static void bfs(int r, int c) {
        Queue<Pos> queue = new LinkedList<>();
        queue.offer(new Pos(r, c));
        visited[r][c] = 1;

        while (!queue.isEmpty()) {
            Pos node = queue.poll();
            int sr = node.r;
            int sc = node.c;

            for (int d = 0; d < 4; d++) {
                int nr = sr + dr[d];
                int nc = sc + dc[d];

                if (nr >= 1 && nr <= n && nc >= 1 && nc <= n) {
                    if (arr[nr][nc] == 0 && visited[nr][nc] == 0) {
                        queue.offer(new Pos(nr, nc));
                        visited[nr][nc] = visited[sr][sc] + 1;
                    }
                }
            }
        }

    }
}
