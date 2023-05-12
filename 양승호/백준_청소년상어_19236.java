import java.util.*;
import java.io.*;

public class 백준_청소년상어_19236 {
    public static int[][] map;
    public static Fish[] fish;
    public static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
    public static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        map = new int[4][4];
        fish = new Fish[17];
        for(int i = 0; i < 4; i++) {
            st  = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < 4; j++) {
                int num = Integer.parseInt(st.nextToken());
                int dir = Integer.parseInt(st.nextToken())-1;
                fish[num] = new Fish(num, i, j, dir, 1);
                map[i][j] = num;
            }
        }

        int shark_x = 0, shark_y = 0;
        int shark_dir = fish[map[0][0]].dir;
        int eat = map[0][0];
        fish[map[0][0]].alive = 0;
        map[0][0] = -1;

        dfs(shark_x, shark_y, shark_dir, eat);

        System.out.println(ans);
    }

    public static void dfs(int shark_x, int shark_y, int shark_dir, int eat) {
        ans = Math.max(ans, eat);

        int[][] subMap = new int[map.length][map.length];
        for(int i = 0; i < map.length; i++) {
            System.arraycopy(map[i], 0, subMap[i], 0, map.length);
        }

        Fish[] subFish = new Fish[fish.length];
        for(int i = 1; i <= 16; i++)
            subFish[i] = new Fish(fish[i].num, fish[i].x, fish[i].y, fish[i].dir, fish[i].alive);

        moveFish();

        for(int i = 1; i < 4; i++) {
            int mx = shark_x + dx[shark_dir] * i;
            int my = shark_y + dy[shark_dir] * i;
            if(mx >= 0 && mx < 4 && my >= 0 && my < 4 && map[mx][my] != 0) {
                int eatFish = map[mx][my];
                int nd = fish[eatFish].dir;
                map[shark_x][shark_y] = 0;
                map[mx][my] = -1;
                fish[eatFish].alive = 0;

                dfs(mx, my, nd, eat+eatFish);

                fish[eatFish].alive = 1;
                map[shark_x][shark_y] = -1;
                map[mx][my] = eatFish;
            }
        }

        for(int j = 0; j < map.length; j++)
            System.arraycopy(subMap[j], 0, map[j], 0, map.length);

        for(int i=1; i<=16; i++)
            fish[i] = new Fish(subFish[i].num, subFish[i].x, subFish[i].y, subFish[i].dir, subFish[i].alive);
    }

    public static void moveFish() {
        for(int i = 1; i < 17; i++) {
            if(fish[i].alive == 0) {
                continue;
            }

            int cnt = 0;
            int dir = fish[i].dir;
            int mx = 0, my = 0;

            while(cnt < 8) {
                dir %= 8;
                fish[i].dir = dir;

                mx = fish[i].x + dx[dir];
                my = fish[i].y + dy[dir];

                if(mx >= 0 && mx < 4 && my >= 0 && my < 4 && map[mx][my] != -1) {
                    if(map[mx][my] == 0) {
                        map[fish[i].x][fish[i].y] = 0;
                        fish[i].x = mx;
                        fish[i].y = my;
                        map[mx][my] = i;
                    } else {
                        int changeFish = fish[map[mx][my]].num;
                        fish[changeFish].x = fish[i].x;
                        fish[changeFish].y = fish[i].y;
                        map[fish[changeFish].x][fish[changeFish].y] = changeFish;
                        fish[i].x = mx;
                        fish[i].y = my;
                        map[mx][my] = i;
                    }
                    break;
                } else {
                    dir++;
                    cnt++;
                }
            }
        }
    }

}

class Fish {
    int num;
    int x;
    int y;
    int dir;
    int alive;

    Fish(int num, int x, int y, int dir, int alive) {
        this.num = num;
        this.x = x;
        this.y = y;
        this.dir = dir;
        this.alive = alive;
    }
}
