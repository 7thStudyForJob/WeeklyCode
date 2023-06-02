import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_2473 {
    static long[] indexes;
    static long answer = Long.MAX_VALUE;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Long[] arr = Arrays.stream(br.readLine().split(" ")).map(Long::parseLong).toArray(Long[]::new);
        Arrays.sort(arr);

        indexes = new long[3];

        for (int i = 0; i < N - 2; i++) {
            findMax(arr, i);
        }



        Arrays.sort(indexes);

        System.out.printf("%d %d %d\n", indexes[0], indexes[1], indexes[2]);
    }


    static void findMax(Long[] arr, int index) {
        int left = index+1;
        int right = arr.length-1;

        while(left < right) {

            long sum = arr[left] + arr[right] + arr[index];
            long absSum = Math.abs(sum);

            // 두 용액 갱신
            if(absSum < answer) {
                indexes[0] = arr[left];
                indexes[1] = arr[right];
                indexes[2] = arr[index];
                answer = absSum;
            }

            if(sum > 0)
                right--;
            else
                left++;
        }
    }
}
