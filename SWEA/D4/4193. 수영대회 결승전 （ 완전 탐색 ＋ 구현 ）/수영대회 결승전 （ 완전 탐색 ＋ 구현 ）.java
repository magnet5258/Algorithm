import java.util.*;

public class Solution {
    static int N;
    static int[][] pool;
    static boolean[][][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static class Node {
        int x, y, time;
        Node(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            pool = new int[N][N];
            visited = new boolean[N][N][3];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    pool[i][j] = sc.nextInt();
                }
            }

            int sx = sc.nextInt();
            int sy = sc.nextInt();
            int ex = sc.nextInt();
            int ey = sc.nextInt();

            int result = bfs(sx, sy, ex, ey);
            System.out.println("#" + test_case + " " + result);
        }
    }

    static int bfs(int sx, int sy, int ex, int ey) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(sx, sy, 0));
        visited[sx][sy][0] = true;

        while (!queue.isEmpty()) {
            Node cur = queue.poll();

            if (cur.x == ex && cur.y == ey) {
                return cur.time;
            }

            int nextTime = cur.time + 1;

            // 이동
            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (visited[nx][ny][nextTime % 3]) continue;
                if (pool[nx][ny] == 1) continue;
                if (pool[nx][ny] == 2 && nextTime % 3 != 0) continue;

                visited[nx][ny][nextTime % 3] = true;
                queue.add(new Node(nx, ny, nextTime));
            }

            boolean shouldWait = false;
            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];
                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (pool[nx][ny] == 2 && nextTime % 3 != 0) {
                    shouldWait = true;
                    break;
                }
            }

            if (shouldWait && !visited[cur.x][cur.y][nextTime % 3]) {
                visited[cur.x][cur.y][nextTime % 3] = true;
                queue.add(new Node(cur.x, cur.y, nextTime));
            }
        }

        return -1;
    }
}
