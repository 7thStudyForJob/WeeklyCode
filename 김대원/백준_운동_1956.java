import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1956 {
    static int V, E;
    static final int MAX = 100000000;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        V = Integer.parseInt(input[0]);
        E = Integer.parseInt(input[1]);
        int[][] dist = new int[V+1][V+1];
        for (int i = 0; i <= V; i++) {
            Arrays.fill(dist[i], MAX);
            dist[i][i] = 0;
        }
        for (int i = 0; i < E; i++) {
            int[] edge = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            dist[edge[0]][edge[1]] = edge[2];
        }

        for (int k = 1; k <= V; k++) {
            for (int r = 1; r <= V; r++) {
                for (int c = 1; c <= V; c++) {
                    if(dist[r][c] > dist[r][k] + dist[k][c]){
                        dist[r][c] = dist[r][k] + dist[k][c];
                    }
                }
            }
        }

        int ans = MAX;
        for (int src = 1; src <= V; src++) {
            for (int dst = 1; dst <= V; dst++) {
                if(src != dst && dist[src][dst] != MAX && dist[dst][src] != MAX){
                    ans = Math.min(ans, dist[src][dst] + dist[dst][src]);
                }
            }
        }
        
        System.out.println(ans == MAX ? -1 : ans);
    }
}
