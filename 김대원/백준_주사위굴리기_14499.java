import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_14499 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int x = Integer.parseInt(inputs[2]);
        int y = Integer.parseInt(inputs[3]);
        int K = Integer.parseInt(inputs[4]);

        int[][] map = new int[N][M];
        for (int r = 0; r < N; r++) {
            inputs = br.readLine().split(" ");
            for (int c = 0; c < M; c++) {
                map[r][c] = Integer.parseInt(inputs[c]);
            }
        }

        inputs = br.readLine().split(" ");

        int[][] dir = {{0, 0},{0, 1},{0, -1},{-1, 0},{1, 0}};
        Dice dice = Dice.getInstance();
        for (int i = 0; i < K; i++) {
            int command = Integer.parseInt(inputs[i]);
            int nx = x + dir[command][0];
            int ny = y + dir[command][1];
            if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
                switch (command) {
                    // 동쪽
                    case 1:
                        dice.rollEast();
                        fillDice(map, nx, ny, dice);
                        break;
                    // 서쪽
                    case 2:
                        dice.rollWest();
                        fillDice(map, nx, ny, dice);
                        break;
                    // 북쪽
                    case 3:
                        dice.rollNorth();
                        fillDice(map, nx, ny, dice);
                        break;
                    // 남쪽
                    case 4:
                        dice.rollSouth();
                        fillDice(map, nx, ny, dice);
                        break;
                }
                x = nx;
                y = ny;
                System.out.println(dice.top);
            }
        }

    }

    static void fillDice(int[][] map, int nx, int ny, Dice dice){
        if(map[nx][ny] == 0){
            map[nx][ny] = dice.bottom;
        }else{
            dice.bottom = map[nx][ny];
            map[nx][ny] = 0;
        }
    }

    static class Dice{
        int top, bottom, right, left, forward, backward;

        private static Dice dice;

        private Dice(){
            this.top = 0;
            this.bottom = 0;
            this.right = 0;
            this.left = 0;
            this.forward = 0;
            this.backward = 0;
        }

        private static Dice getInstance(){
            if(dice == null){
                dice = new Dice();
            }

            return dice;
        }

        void rollNorth(){
            int temp = top;
            top = forward;
            forward = bottom;
            bottom = backward;
            backward = temp;
        }
        void rollSouth(){
            int temp = top;
            top = backward;
            backward = bottom;
            bottom = forward;
            forward = temp;
        }
        void rollEast(){
            int temp = top;
            top = left;
            left = bottom;
            bottom = right;
            right = temp;
        }
        void rollWest(){
            int temp = top;
            top = right;
            right = bottom;
            bottom = left;
            left = temp;
        }
    }
}
