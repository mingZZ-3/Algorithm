import java.util.*;

class Solution {
    char[][] graph;
    int R, C;
    int[] S, E, L;
    
    public int solution(String[] maps) {
        R = maps.length;
        C = maps[0].length();
        
        graph = new char[R][C];
        for (int i=0; i < R; i++) {
            for (int j=0; j < C; j++) {
                graph[i][j] = maps[i].charAt(j);

                if (graph[i][j] == 'S') {
                    S = new int[]{i, j};
                } else if (graph[i][j] == 'E') {
                    E = new int[]{i, j};
                } else if (graph[i][j] == 'L') {
                    L = new int[]{i, j};
                }
            }
        }
        
        // s -> l
        int sl = BFS(S, L);
        if (sl == -1) return -1;
        
        // l -> e
        int le = BFS(L, E);
        if (le == -1) return -1;
        
        return sl + le;
    }
    
    int[] dirR = {1, -1, 0, 0};
    int[] dirC = {0, 0, 1, -1};
    
    public int BFS(int[] s, int[] e) {
        Queue<int[]> que = new ArrayDeque<>();
        boolean[][] visited = new boolean[R][C];
        que.add(new int[]{s[0], s[1], 0});
        visited[s[0]][s[1]] = true;
        
        while(!que.isEmpty()) {
            int[] top = que.poll();
            
            if (top[0] == e[0] && top[1] == e[1]) return top[2];
            
            for (int i=0; i < 4; i++) {
                int nr = top[0] + dirR[i];
                int nc = top[1] + dirC[i];
                
                if (inRange(nr, nc) && graph[nr][nc] != 'X') {
                    if (!visited[nr][nc]) {
                        visited[nr][nc] = true;
                        que.add(new int[]{nr, nc, top[2] + 1});
                    }
                }
            }
        }
        
        return -1;
    } 
    
    public boolean inRange(int r, int c) {
        return (r >= 0) && (c >= 0) && (r < R) && (c < C);
    }
}