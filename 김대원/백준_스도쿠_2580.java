import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class BOJ_2580 {
    static int[][] sudoku;
    static ArrayList<int[]> zeros;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sudoku = new int[9][9];
        zeros = new ArrayList<>();
        for (int r = 0; r < 9; r++) {
            String[] inputs = br.readLine().split(" ");
            for (int c = 0; c < 9; c++) {
                sudoku[r][c] = Integer.parseInt(inputs[c]);
                if(sudoku[r][c] == 0){
                    zeros.add(new int[]{r, c});
                }
            }
        }

        // 백트래킹으로 채워보기
        DFS(0);
    }

    static boolean flag;

    static void DFS(int idx){
        if(flag) return;

        if(idx == zeros.size()){
            for (int r = 0; r < 9; r++) {
                for (int c = 0; c < 9; c++) {
                    System.out.printf("%d ", sudoku[r][c]);
                }
                System.out.println();
            }
            flag = true;
            return;
        }

        int[] point = zeros.get(idx);
        // 가능 한 값 찾기
        boolean[] possible = check(point[0], point[1]);

        for (int i = 1; i < 10; i++) {
            if(!possible[i]){
                sudoku[point[0]][point[1]] = i;
                DFS(idx + 1);
                sudoku[point[0]][point[1]] = 0;
            }
        }

    }

    // 가능한 값 체크
    static boolean[] check(int row, int col){
        // 가로 체크
        boolean[] v = new boolean[10];
        for (int i = 0; i < 9; i++) {
            v[sudoku[row][i]] = true;
        }
        // 세로 체크
        for (int i = 0; i < 9; i++) {
            v[sudoku[i][col]] = true;
        }
        // 3*3 체크
        int rStart = (row / 3) * 3;
        int cStart = (col / 3) * 3;
        for (int r = rStart; r < rStart + 3; r++) {
            for (int c = cStart; c < cStart + 3; c++) {
                v[sudoku[r][c]] = true;
            }
        }

        return v;
    }
}
