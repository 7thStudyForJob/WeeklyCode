import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_19238 {
    static int N, M, fuel;
    // 0 : 통과, 1 : 벽, 2 : 출발점, 3 : 도착점
    static int[][] map;
    static Point start;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        fuel = Integer.parseInt(inputs[2]);

        map = new int[N + 1][N + 1];
        for (int r = 1; r <= N; r++) {
            inputs = br.readLine().split(" ");
            for (int c = 1; c <= N; c++) {
                map[r][c] = Integer.parseInt(inputs[c-1]);
            }
        }

        inputs = br.readLine().split(" ");
        start = new Point(Integer.parseInt(inputs[0]), Integer.parseInt(inputs[1]));

        HashMap<Point, Point> course = new HashMap<>();
        for (int i = 0; i < M; i++) {
            inputs = br.readLine().split(" ");
            int sr = Integer.parseInt(inputs[0]);
            int sc = Integer.parseInt(inputs[1]);
            int dr = Integer.parseInt(inputs[2]);
            int dc = Integer.parseInt(inputs[3]);
            map[sr][sc] = 2;
            course.put(new Point(sr, sc), new Point(dr, dc));
        }

        while(course.size() > 0){
            // 시작 점에서 거리 체크
            start = getStart();

            // 연료가 바닥났을 경우
            if(start == null){
                System.out.println(-1);
                return;
            }else{
                // 시작점에서 도착점까지
                map[start.r][start.c] = 0;
                start.dist = 0;

                // 도착지 찾기
                Point src = null;
                for (Point temp: course.keySet()) {
                    if(start.r == temp.r && start.c == temp.c){
                        src = temp;
                        break;
                    }
                }

                int distance = getEnd(course.get(src));

                if(distance == -1){
                    // 도착 못하는 경우 or 연료를 다 쓴 경우
                    System.out.println(-1);
                    return;
                }else {
                    // 도착한 경우
                    fuel += distance * 2;

                }

                start = course.get(src);
                course.remove(src);
            }
        }

        System.out.println(fuel);
    }

    static int[][] dir = {{-1, 0},{0,1},{1,0},{0,-1}};
    // 시작점을 찾는 메서드
    static Point getStart(){
        // BFS로 거리 체크
        PriorityQueue<Point> targets = new PriorityQueue<>((o1, o2) -> {
            if(o1.dist == o2.dist){
                if(o1.r == o2.r){
                    return o1.c - o2.c;
                }
                return o1.r - o2.r;
            }
            return o1.dist - o2.dist;
        });

        Queue<Point> q = new LinkedList<>();
        q.offer(start);
        boolean[][] v = new boolean[N+1][N+1];
        v[start.r][start.c] = true;

        while(!q.isEmpty()){
            Point cur = q.poll();

            // 가장 가까운 시작점을 찾으면
            if(map[cur.r][cur.c] == 2){
                targets.offer(cur);
            }

            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dir[d][0];
                int nc = cur.c + dir[d][1];
                // 범위 체크, 벽 체크
                if(nr >= 1 && nr <= N && nc >= 1 && nc <= N && map[nr][nc] != 1 && !v[nr][nc]){
                    v[nr][nc] = true;
                    q.offer(new Point(nr, nc, cur.dist + 1));
                }
            }
        }

        // 다 벽으로 막혀있는 경우
        if(targets.isEmpty()){
            return null;
        }else{
            fuel -= targets.peek().dist;
            //연료를 다 쓴 경우
            if(fuel <= 0){
                return null;
            }else{
                return targets.peek();
            }
        }
    }
    static int getEnd(Point dist){
        // BFS로 거리 체크
        Queue<Point> q = new LinkedList<>();
        q.offer(start);
        boolean[][] v = new boolean[N+1][N+1];
        v[start.r][start.c] = true;

        while(!q.isEmpty()){
            Point cur = q.poll();

            // 도착점에 도착하면 거리 감소
            if(cur.r == dist.r && cur.c == dist.c){
                fuel -= cur.dist;
                return fuel >= 0 ? cur.dist : -1;
            }

            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dir[d][0];
                int nc = cur.c + dir[d][1];
                // 범위 체크, 벽 체크
                if(nr >= 1 && nr <= N && nc >= 1 && nc <= N && map[nr][nc] != 1 && !v[nr][nc]){
                    v[nr][nc] = true;
                    q.offer(new Point(nr, nc, cur.dist + 1));
                }
            }
        }

        return -1;
    }

    static class Point {
        int r, c, dist;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public Point(int r, int c, int dist) {
            this.r = r;
            this.c = c;
            this.dist = dist;
        }
    }
}
