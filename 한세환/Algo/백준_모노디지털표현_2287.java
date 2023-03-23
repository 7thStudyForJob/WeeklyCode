package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main_2287 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int num = Integer.parseInt(br.readLine());
        int testCases = Integer.parseInt(br.readLine());

        Set<Integer>[] set = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            set[i] = new HashSet<>();
        }

        int temp = 0;
        for (int i = 1; i <= 8; i++) {
            temp = temp * 10 + num;
            set[i].add(temp);
        }

        int kLen = 0;
        for (int i = 1; i <= 8; i++) {
            for (int j = 1; j <= i; j++) {
                kLen = i + j;

                if (kLen > 8) {
                    continue;
                }

                for (int y : set[i]) {
                    for (int x : set[j]) {

                        // +
                        set[kLen].add(x + y);

                        // -
                        if (x != y)
                            set[kLen].add(Math.abs(x - y));

                        // *
                        set[kLen].add(x * y);

                        // /(나누기)
                        if (y > x)
                            set[kLen].add(y / x);
                        else
                            set[kLen].add(x / y);
                    }
                }
            }
        }

        for (int i = 0; i < testCases; i++) {
            int targetNum = Integer.parseInt(br.readLine());

            int check = -1;

            for (int j = 1; j <= 8; j++) {
                if (set[j].contains(targetNum)) {
                    check = j;
                    break;
                }
            }

            if (check == -1)
                sb.append("NO").append('\n');
            else
                sb.append(check).append('\n');
        }

        System.out.println(sb.toString());

    }

}
