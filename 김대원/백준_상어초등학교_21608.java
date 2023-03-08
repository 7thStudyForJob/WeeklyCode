import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class BOJ_21608 {
    // 사방 탐색용 배열
    static int[][] dir = {{-1 , 0},{1, 0},{0, -1},{0, 1}};
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        // int보단 추후에 만족도 계산을 위해 Student로 만듬
        Student[][] map = new Student[N+1][N+1];
        // 중복 체크를 위한 배열
        boolean[][] v = new boolean[N+1][N+1];
        // 값 집어 넣기
        ArrayList<Student> students = new ArrayList<>();
        String[] inputs = null;
        for (int i = 0; i < N*N; i++) {
            inputs = br.readLine().split(" ");

            int s = Integer.parseInt(inputs[0]);
            int[] friends = new int[4];
            for (int j = 0; j < 4; j++) {
                friends[j] = Integer.parseInt(inputs[j+1]);
            }

            students.add(new Student(s, friends));
        }

        // 자리 탐색
        for (Student s: students) {
            // 이 풀이의 핵심 -> 조건에 맞춰서 우선순위 큐 생성
            // 친구가 있는 칸의 수 -> 빈 칸의 수 -> 행과 열이 낮은 순서
            PriorityQueue<Seat> candidates = new PriorityQueue<>((o1, o2) -> {
                if(o1.friendPoint == o2.friendPoint){
                    if(o1.emptyPoint == o2.emptyPoint){
                        if(o1.r == o2.r){
                            return o1.c - o2.c;
                        }else{
                            return o1.r - o2.r;
                        }
                    }else{
                        return o2.emptyPoint - o1.emptyPoint;
                    }
                }else{
                    return o2.friendPoint - o1.friendPoint;
                }
            });

            // 전체 탐색
            for (int r = 1; r <= N; r++) {
                for (int c = 1; c <= N; c++) {
                    if(v[r][c]) continue;
                    // 친구 탐색
                    int empty = 0;
                    int friend = 0;
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dir[d][0];
                        int nc = c + dir[d][1];

                        if(nr >= 1 && nr <= N && nc >= 1 && nc <= N){
                            if(map[nr][nc] == null){
                                empty++;
                            }else{
                                for (int f = 0; f < 4; f++) {
                                    if(s.friends[f] == map[nr][nc].num){
                                        friend++;
                                    }
                                }
                            }
                        }
                    }
                    candidates.add(new Seat(r, c, empty, friend));
                }
            }

            // 최적 값 찾기
            Seat best = candidates.poll();
            map[best.r][best.c] = s;
            v[best.r][best.c] = true;
            //System.out.println(best);
        }

        // 만족도 계산
        int content = 0;
        for (int r = 1; r <= N; r++) {
            for (int c = 1; c <= N; c++) {
                Student s = map[r][c];
                int friend = 0;
                for (int d = 0; d < 4; d++) {
                    int nr = r + dir[d][0];
                    int nc = c + dir[d][1];
                    if(nr >= 1 && nr <= N && nc >= 1 && nc <= N){
                        for (int f = 0; f < 4; f++) {
                            if(s.friends[f] == map[nr][nc].num){
                                friend++;
                            }
                        }
                    }
                }
                content += Math.pow(10, friend-1);
            }
        }

        System.out.println(content);
    }

    // 자리 후보들
    static class Seat {
        int r, c;
        int emptyPoint;
        int friendPoint;

        public Seat(int r, int c, int emptyPoint, int friendPoint) {
            this.r = r;
            this.c = c;
            this.emptyPoint = emptyPoint;
            this.friendPoint = friendPoint;
        }

        @Override
        public String toString() {
            return "Seat{" +
                    "r=" + r +
                    ", c=" + c +
                    ", emptyPoint=" + emptyPoint +
                    ", friendPoint=" + friendPoint +
                    '}';
        }
    }

    // 학생 정보를 가지고 있는 객체
   static class Student{
        int num;
        int[] friends;

        public Student(int num, int[] friends) {
            this.num = num;
            this.friends = friends;
        }
    }
}
