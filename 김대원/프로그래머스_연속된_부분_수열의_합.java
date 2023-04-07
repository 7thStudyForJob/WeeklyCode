package level2;

import java.util.Arrays;
import java.util.PriorityQueue;

public class 연속된_부분_수열의_합 {
    static int[] sequence = {1, 2, 3, 4, 5};
    static int k = 14;
    // 투 포인터 각
    public static void main(String[] args) {
        int left = 0;
        int right = 1;
        int sum = sequence[0];
        // 길이가 1
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            if(o1.length == o2.length){
                if(o1.length == 1){
                    return o1[0] - o2[0];
                }
                // 2일 때
                else{
                    if((o1[1] - o1[0]) == (o2[1] - o2[0])){
                        return o1[0] - o2[0];
                    }
                    return (o1[1] - o1[0]) - (o2[1] - o2[0]);
                }
            }
            return o1.length - o2.length;
        });

        // 하나짜리 체크
        for (int i = 0; i < sequence.length; i++) {
            if(sequence[i] == k){
                pq.offer(new int[]{i});
            }
        }

        while(right < sequence.length && left <= right){
            if(sum == k){
                pq.offer(new int[]{left, right});
                sum -= sequence[left];
                left++;
            }else if(sum < k){
                sum += sequence[right];
                right++;
            }else{
                sum -= sequence[left];
                left++;
            }
        }

        int[] idx = pq.poll();
        // 임시 방편
        if(idx == null){
            sum = 0;
            for (int i = 0; i < sequence.length; i++) {
                sum += sequence[i];
            }
            for (int i = 0; i < sequence.length; i++) {
                if(sum == k){
                    idx = new int[]{i,sequence.length};
                    break;
                }
                sum -= sequence[i];
            }
        }

        int[] answer = null;
        if (idx.length == 1) {
            answer = new int[]{idx[0], idx[0]};
        } else {
            answer = new int[]{idx[0], idx[1] - 1};
        }


        System.out.println(Arrays.toString(answer));
    }
}
