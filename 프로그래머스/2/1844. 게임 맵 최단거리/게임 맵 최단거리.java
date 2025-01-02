import java.util.*;

class Solution {
    
    int[] dirR = {0, 0, -1, 1};
    int[] dirC = {-1, 1, 0, 0};
    
    public int solution(int[][] maps) {
        int answer = -1;
        int n = maps.length;
        int m = maps[0].length;
        
        // BFS
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> que = new ArrayDeque<>();
        que.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        
        while(!que.isEmpty()) {
            int[] top = que.remove();
            
            if (top[0] == n-1 && top[1] == m-1) {
                answer = top[2];
                break;
            }
            
            for (int i=0; i<4; i++) {
                int newR = top[0] + dirR[i];
                int newC = top[1] + dirC[i];
                
                if (inRange(newR, newC, n, m) && maps[newR][newC] == 1) {
                    if (!visited[newR][newC]) {
                        que.add(new int[]{newR, newC, top[2] + 1});
                        visited[newR][newC] = true; 
                    }
                }
            }
        }
        
        return answer;
    }

    public boolean inRange(int r, int c, int n, int m) {
        return (r >= 0) && (c >= 0) && (r < n) && (c < m);
    }
}