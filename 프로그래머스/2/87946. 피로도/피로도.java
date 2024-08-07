class Solution {
    static boolean[] visited;
    static int cnt;

    public static int solution(int k, int[][] dungeons) {
        cnt = 0;
        visited = new boolean[dungeons.length];

        dfs(0, k, dungeons);

        return cnt;
    }

    private static void dfs(int depth, int k, int[][] dungeons) {
        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i] || dungeons[i][0] > k) {
                continue;
            }
            visited[i] = true;
            dfs(depth + 1, k - dungeons[i][1], dungeons);
            visited[i] = false;
        }
        cnt = Math.max(cnt, depth);
    }
}
