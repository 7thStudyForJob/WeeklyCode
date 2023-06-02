import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_19236 {
    static int[][] dir = {{0, 0}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
    static Fish[][] map;
    static ArrayList<Order> order;
    public static void main(String[] args) throws Exception {
        // 초기값 세팅
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        map = new Fish[4][4];
        order = new ArrayList<>();
        for (int r = 0; r < 4; r++) {
            int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int c = 0; c < 4; c++) {
                map[r][c] = new Fish(input[c*2], input[c*2+1]);
                order.add(new Order(map[r][c].value , r, c));
            }
        }
        order.sort(Comparator.comparingInt(e -> e.val));

        Fish shark = new Fish(map[0][0].value, map[0][0].direction);
        map[0][0].status = -1;
        order.removeIf(e -> e.val == map[0][0].value);

        stack = new Stack<>();
        stack.push(map[0][0].value);

        Backtracking(shark, 0, 0, 0);


        System.out.println(answer);
    }
    // print
    static void print(){
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                System.out.printf("%d ", map[r][c].status == 1 ? map[r][c].value : (map[r][c].status == -1) ? -1 : 0);
            }
            System.out.println();
        }
    }
    // 이동 체크
    static boolean isMovable(int r, int c){
        if(r >= 0 && r < 4 && c >= 0 && c < 4 && map[r][c].status != -1){
            return true;
        }else{
            return false;
        }
    }

    // 물고기 이동
    static void fishMove(){
        for (Order o: order) {
            int nr = o.r + dir[map[o.r][o.c].direction][0];
            int nc = o.c + dir[map[o.r][o.c].direction][1];

            // 이동 가능 -> 모서리가 아니고, 상어가 아닐 때
            if(isMovable(nr, nc)){
                move(o, nr, nc);
            }
            // 이동 불가능 -> 45도 회전하면서 이동 가능한지 체크
            else{
                for (int d = 0; d < 7; d++) {
                    map[o.r][o.c].direction++;
                    if(map[o.r][o.c].direction > 8){
                        map[o.r][o.c].direction = 1;
                    }
                    nr = o.r + dir[map[o.r][o.c].direction][0];
                    nc = o.c + dir[map[o.r][o.c].direction][1];
                    if(isMovable(nr, nc)){
                        move(o, nr, nc);
                        break;
                    }
                }
            }
        }
    }

    private static void move(Order o, int nr, int nc) {
        // 빈 칸일 때
        if(map[nr][nc].status == 0){
            // 지도 업데이트
            Fish temp = map[o.r][o.c];
            map[o.r][o.c] = map[nr][nc];
            map[nr][nc] = temp;
            o.r = nr;
            o.c = nc;
        }
        // 물고기가 있는 칸일 때
        else if(map[nr][nc].status == 1){
            // 지도 위치 변경
            Fish tempVal = map[o.r][o.c];
            map[o.r][o.c] = map[nr][nc];
            map[nr][nc] = tempVal;
            // order 위치 변경
            for (Order oo: order) {
                if(o.val == oo.val) continue;
                if(oo.r == nr && oo.c == nc){
                    int tr = o.r;
                    int tc = o.c;
                    o.r = nr;
                    o.c = nc;
                    oo.r = tr;
                    oo.c = tc;
                    break;
                }
            }
        }
    }

    static int answer = 0;
    // 시뮬레이션
    static Stack<Integer> stack;
    static void Backtracking(Fish shark, int r, int c, int step){
        //System.out.printf("shark : %d, %d, %d, %d, %d\n", shark.value, shark.direction, r, c, step);
        // 물고기 이동
        fishMove();
        Fish[][] prevMap = new Fish[4][4];
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 4; col++) {
                prevMap[row][col] = new Fish(map[row][col].value, map[row][col].direction, map[row][col].status);
            }
        }
        //print();

        Fish prev = new Fish(shark.value, shark.direction);
        ArrayList<Order> prevOrder = new ArrayList<>();
        for (int i = 0; i < order.size(); i++) {
            prevOrder.add(new Order(order.get(i).val, order.get(i).r, order.get(i).c));
        }
        // 상어 이동
        int nr = r + dir[shark.direction][0];
        int nc = c + dir[shark.direction][1];

        while(nr >= 0 && nr < 4 && nc >= 0 && nc < 4){
            if(map[nr][nc].status == 1) {
                // 이동 할 수 있는 칸 -> 잡아 먹음
                map[r][c].status = 0;
                map[nr][nc].status = -1;
                shark.value += map[nr][nc].value;
                shark.direction = map[nr][nc].direction;
                int finalNr = nr;
                int finalNc = nc;
                order.removeIf(e -> e.val == map[finalNr][finalNc].value);
                stack.push(map[nr][nc].value);

                Backtracking(shark, nr, nc, step + 1);
                // 백트래킹
                for (int row = 0; row < 4; row++) {
                    for (int col = 0; col < 4; col++) {
                        map[row][col] = new Fish(prevMap[row][col].value,prevMap[row][col].direction,prevMap[row][col].status);
                    }
                }
                shark = new Fish(prev.value, prev.direction, prev.status);
                order.clear();
                for (int i = 0; i < prevOrder.size(); i++) {
                    order.add(new Order(prevOrder.get(i).val, prevOrder.get(i).r, prevOrder.get(i).c));
                }
                stack.pop();
            }
            nr += dir[shark.direction][0];
            nc += dir[shark.direction][1];
        }

        //System.out.println(stack.toString());
        answer = Math.max(answer, shark.value);
    }

    static class Fish {
        // status : 1 (물고기), 0 (빈 칸), -1 (상어)
        int value, direction, status;

        public Fish(int value, int direction) {
            this.value = value;
            this.direction = direction;
            this.status = 1;
        }

        public Fish(int value, int direction, int status) {
            this.value = value;
            this.direction = direction;
            this.status = status;
        }

        @Override
        public String toString() {
            return "Fish{" +
                    "value=" + value +
                    ", direction=" + direction +
                    ", status=" + status +
                    '}';
        }
    }

    static class Order{
        int val, r, c;

        public Order(int val, int r, int c) {
            this.val = val;
            this.r = r;
            this.c = c;
        }

        @Override
        public String toString() {
            return "Order{" +
                    "val=" + val +
                    ", r=" + r +
                    ", c=" + c +
                    '}';
        }
    }
}
