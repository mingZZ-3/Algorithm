class Solution {
    int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        backtrack(k, dungeons, 0, new boolean[dungeons.length]);
        return answer;
    }
    
    public void backtrack(int k, int[][] dungeons, int cnt, boolean[] visited) {
        if (cnt > answer)
            answer = cnt;
        
        for (int i=0; i<dungeons.length; i++) {
            if (!visited[i] && k >= dungeons[i][0]) { // 던전에 들어갈 수 있으면
                visited[i] = true;
                backtrack(k - dungeons[i][1], dungeons, cnt + 1, visited);
                visited[i] = false;
            }
        }
    }
}