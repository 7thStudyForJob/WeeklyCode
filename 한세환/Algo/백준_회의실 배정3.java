package boj;

import java.io.*;
import java.util.*;

public class Main_19622 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        int[][] arr = new int[testCase+2][2];

        for(int i=2;i<=testCase+1;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken(); st.nextToken();
            int cur = Integer.parseInt(st.nextToken());
            arr[i][0] = Math.max(arr[i-1][0], arr[i-1][1]);
            arr[i][1] = Math.max(arr[i-1][0], arr[i-2][1]) + cur;
        }
        System.out.print(Math.max(arr[testCase+1][0], arr[testCase+1][1]));

    }
}
