import java.util.PriorityQueue;

// 처음에 다 평가를 해놓고 새로 들어갈 때만 뺄까?

public class 더_맵게 {
    static int[] scoville = {1, 2, 3, 9, 10, 12};
    static int K = 7;
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s: scoville) {
            pq.offer(s);
        }

        int count = 0;
        try{
            while(true){
                int l1 = pq.poll();
                if(l1 >= K){
                    break;
                }
                int l2 = pq.poll();
                int ns = l1 + l2*2;
                pq.offer(ns);
                count++;
            }

            System.out.println(count);;
        }catch(Exception e){
            System.out.println(-1);
        }
    }
}
