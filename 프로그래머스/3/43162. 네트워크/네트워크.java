import java.util.*;

class Solution {
    boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int cnt = 0;
        visited = new boolean[n];
        
        for (int i=0; i < n; i++) {
            if (visited[i]) continue;
            
            DFS(computers, n, i);
            cnt++;
        }
        
        return cnt;
    }
    
    public void DFS(int[][] computers, int n, int node) {
        visited[node] = true;
        
        for (int j=0; j < n; j++) {
            if (!visited[j] && computers[node][j] == 1) {
                DFS(computers, n, j);
            }
        }
    }
}