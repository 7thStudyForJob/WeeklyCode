import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class BOJ_21924 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.val));
        long answer = 0;
        for (int i = 0; i < M; i++) {
            inputs = br.readLine().split(" ");
            int src = Integer.parseInt(inputs[0]);
            int dst = Integer.parseInt(inputs[1]);
            int val = Integer.parseInt(inputs[2]);
            answer += val;

            pq.offer(new Node(src, dst, val));

        }

        int[] parent = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        int count = 0;
        while(!pq.isEmpty()){
            Node cur = pq.poll();

            if(getParent(cur.src, parent) != getParent(cur.dst, parent)){
                union(cur.src, cur.dst, parent);
                answer -= cur.val;
                count++;
            }
        }

        System.out.println(count == N - 1 ? answer : -1);
    }

    static int getParent(int i, int[] parent){
        if(parent[i] == i) return i;
        return getParent(parent[i], parent);
    }

    static void union(int a, int b, int[] parent){
        a = getParent(a, parent);
        b = getParent(b, parent);

        if(a > b){
            parent[a] = b;
        }else{
            parent[b] = a;
        }
    }

    static class Node{
        int src, dst, val;

        public Node(int src, int dst, int val) {
            this.src = src;
            this.dst = dst;
            this.val = val;
        }
    }
}
