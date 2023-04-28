import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 백준_16235_나무재테크 {
    static int dx[] = { -1, -1, -1, 0, 1, 1, 1, 0 };
    static int dy[] = { -1, 0, 1, 1, 1, 0, -1, -1 };

    static class Tree implements Comparable<Tree> {
        int r, c, age;

        public Tree(int r, int c, int age) {
            super();
            this.r = r;
            this.c = c;
            this.age = age;
        }

        @Override
        public int compareTo(Tree o) {
            return this.age - o.age;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n, m, k;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int eng[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {

                eng[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ArrayList<Tree> list = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            list.add(new Tree(r, c,	Integer.parseInt(st.nextToken())));
        }

        int map[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = 5;
            }
        }
        for (int year = 0; year < k; year++) {
            ArrayList<Tree> temp = new ArrayList<>();
            ArrayList<Tree> death = new ArrayList<>();
            for (Tree tree : list) {
                if (map[tree.r][tree.c] > 0 && map[tree.r][tree.c] >= tree.age) {
                    map[tree.r][tree.c] -= tree.age;
                    tree.age += 1;
                    temp.add(new Tree(tree.r, tree.c, tree.age));
                } else {
                    death.add(new Tree(tree.r, tree.c, tree.age));
                }
            }
            for (int j = 0; j<death.size(); j++) {
                Tree tree = death.get(j);
                map[tree.r][tree.c] += (tree.age / 2);
            }
            list.clear();
            for (Tree tree : temp) {
                if (tree.age % 5 == 0) {
                    for (int j = 0; j < 8; j++) {
                        int nr = tree.r + dx[j];
                        int nc = tree.c + dy[j];
                        if (nr < 0 || nr >= n || nc < 0 || nc >= n)
                            continue;
                        list.add(new Tree(nr, nc, 1));
                    }
                }
            }
            list.addAll(temp);
            for (int j = 0; j < map.length; j++) {
                for (int j2 = 0; j2 < map.length; j2++) {
                    map[j][j2] += eng[j][j2];
                }
            }
        }
        System.out.println(list.size());
    }
}