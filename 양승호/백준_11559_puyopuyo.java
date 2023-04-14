import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.List;
import java.util.ArrayList;
public class 백준_11559_puyopuyo {
    static int r,c;
    static int cnt=0;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};
    static char[][] board;
    static boolean[][] visited;
    static boolean finished;
    static Queue<puyo> que;
    static List<int[]> list = new ArrayList<>();
    static class puyo{
        int x;
        int y;
        char color;

        puyo(int x, int y, char color){
            this.x = x;
            this.y = y;
            this.color = color;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        r = 12;
        c = 6;
        board = new char[r][c];
        for(int i=0;i<r;i++){
            String str = br.readLine();
            for(int j=0;j<c;j++){
                board[i][j] = str.charAt(j);
            }
        }

        outer : while(true){
            visited = new boolean[12][6];
            finished = true;
            for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    if(board[i][j] != '.' && !visited[i][j]){
                        list = new ArrayList<>();
                        bfs(i,j);

                        if(list.size() >= 4){
                            finished = false;
                            for(int[] arr : list){
                                board[arr[0]][arr[1]] = '.';
                            }
                        }
                    }
                }
            }

            if(finished) break;
            drop();
            cnt++;
        }

        System.out.println(cnt);
    }

    public static void bfs(int x, int y){
        que = new LinkedList<>();
        visited[x][y] = true;
        que.add(new puyo(x,y,board[x][y]));
        list.add(new int[]{x,y});

        while(!que.isEmpty()){
            puyo p = que.poll();
            for(int i=0;i<4;i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(isRange(nx,ny) && board[nx][ny] == p.color && !visited[nx][ny]){
                    que.add(new puyo(nx,ny,p.color));
                    list.add(new int[]{nx,ny});
                    visited[nx][ny] = true;
                }
            }
        }
    }

    public static void drop(){
        for(int i=0;i<c;i++){
            for(int j=0;j<r;j++){
                if(board[j][i] != '.'){
                    que.add(new puyo(j,i,board[j][i]));
                    board[j][i] = '.';
                }
            }

            for(int j=0;j<que.size();j++){
                puyo p = que.poll();
                board[j][i] = p.color;
            }
        }
    }

    public static boolean isRange(int x,int y){
        if(x < r && y < c && x >= 0 && y >= 0){
            return true;
        }

        return false;
    }
}
