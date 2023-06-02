import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class BOJ_20056 {
    static int N, M, K;
    static int[][] dir = {{-1, 0},{-1, 1},{0, 1},{1, 1},{1, 0},{1, -1},{0, -1},{-1, -1}};
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        K = Integer.parseInt(inputs[2]);

        ArrayList<Fireball> magic = new ArrayList<>();


        for (int i = 0; i < M; i++) {
            inputs = br.readLine().split(" ");
            int r = Integer.parseInt(inputs[0]);
            int c = Integer.parseInt(inputs[1]);
            int mass = Integer.parseInt(inputs[2]);
            int speed = Integer.parseInt(inputs[3]);
            int direction = Integer.parseInt(inputs[4]);
            Point p = new Point(r - 1, c - 1);
            Fireball f = new Fireball(p, mass, speed, direction);
            magic.add(f);
        }

        for (int cnt = 0; cnt < K; cnt++) {
            // 파이어볼 이동
            for (Fireball f: magic) {
                // 범위 체크
                int nr = f.p.r + dir[f.d][0] * f.s;
                int nc = f.p.c + dir[f.d][1] * f.s;
                if(nr >= N){
                    nr %= N;
                }else if(nr < 0){
                    nr = Math.floorMod(nr, N);
                }

                if(nc >= N){
                    nc %= N;
                }else if(nc < 0){
                    nc = Math.floorMod(nc, N);
                }

                f.p.r = nr;
                f.p.c = nc;
            }

            // 개수 체크는 어떻게 -> stream 공부하기
            Map<Point, List<Fireball>> counter = magic.stream().collect(Collectors.groupingBy(Fireball::getP));

            // 합치고 나누기
            magic.clear();
            for (Point p: counter.keySet() ) {
                int totalMass = 0;
                int totalSpeed = 0;
                int size = counter.get(p).size();
                boolean isOdd = true, isEven = true;
                if(size > 1) {
                    for (Fireball f : counter.get(p)) {
                        totalMass += f.m;
                        totalSpeed += f.s;
                        if(f.d % 2 == 0){
                            isOdd = false;
                        }else{
                            isEven = false;
                        }
                    }

                    for (int i = 0; i < 4; i++) {
                        Fireball temp = new Fireball(new Point(p.r, p.c),
                                (int)Math.floor(totalMass*1.0 / 5),
                                (int)Math.floor(totalSpeed*1.0 / size),
                                isEven || isOdd ? i*2 : i*2+1);
                        if(temp.m > 0) {
                            magic.add(temp);
                        }
                    }
                }else{
                    magic.add(counter.get(p).get(0));
                }
            }
        }
        int answer = 0;
        for (Fireball f: magic) {
            answer += f.m;
        }
        System.out.println(answer);
    }

    static class Point{
        int r, c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            return r == point.r && c == point.c;
        }

        @Override
        public int hashCode() {
            return Objects.hash(r, c);
        }

        @Override
        public String toString() {
            return "Point{" +
                    "r=" + r +
                    ", c=" + c +
                    '}';
        }
    }

    static class Fireball{
        Point p;
        int m, s, d;

        public Fireball(Point p, int m, int s, int d) {
            this.p = p;
            this.m = m;
            this.s = s;
            this.d = d;
        }

        public Point getP() {
            return p;
        }

        @Override
        public String toString() {
            return "Fireball{" +
                    "p=" + p +
                    ", m=" + m +
                    ", s=" + s +
                    ", d=" + d +
                    '}';
        }
    }
}
