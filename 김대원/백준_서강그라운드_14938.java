import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_14938 {
    static HashMap<Integer, ArrayList<Node>> graph;
    static int N, M, R;
    static final int MAX = 10000000;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        R = Integer.parseInt(inputs[2]);

        int[] vals = new int[N+1];
        inputs = br.readLine().split(" ");
        for (int i = 1; i <= N; i++) {
            vals[i] = Integer.parseInt(inputs[i-1]);
        }
        
        graph = new HashMap<>();

        for (int i = 1; i <= N; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < R; i++) {
            inputs = br.readLine().split(" ");
            int src = Integer.parseInt(inputs[0]);
            int dst = Integer.parseInt(inputs[1]);
            int val = Integer.parseInt(inputs[2]);

            graph.get(src).add(new Node(dst, val));
            graph.get(dst).add(new Node(src, val));
        }

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            int[] dist = dijkstra(i);
            int sum = 0;
            for (int d = 1; d <= N; d++) {
                if(dist[d] <= M){
                    sum += vals[d];
                }
            }
            answer = Math.max(answer, sum);
        }

        System.out.println(answer);
    }

    static int[] dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.val));

        int[] dist = new int[N+1];
        Arrays.fill(dist, MAX);
        dist[start] = 0;
        pq.offer(new Node(start, 0));

        while(!pq.isEmpty()){
            Node cur = pq.poll();

            if(dist[cur.dst] < cur.val) continue;

            for (Node n: graph.get(cur.dst)) {
                if(dist[n.dst] > dist[cur.dst] + n.val){
                    dist[n.dst] = dist[cur.dst] + n.val;
                    pq.offer(new Node(n.dst, dist[n.dst]));
                }
            }
        }

        return dist;
    }


    static class Node{
        int dst, val;

        public Node(int dst, int val) {
            this.dst = dst;
            this.val = val;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "dst=" + dst +
                    ", val=" + val +
                    '}';
        }
    }
}
