import java.util.*;

class Solution {
    // 동, 서, 남, 북
    List<Integer> dirX = new ArrayList<>(Arrays.asList(0, 0, 1, -1));
    List<Integer> dirY = new ArrayList<>(Arrays.asList(1, -1, 0, 0));
    int[][] visited;
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        visited = new int[n][m];
        for (int i=0; i < n; i++) {
            for (int j=0; j < m; j++) {
                visited[i][j] = -1;
            }
        }
        
        // BFS
        Queue<Pos> que = new ArrayDeque<>();
        que.add(new Pos(0,0));
        
        visited[0][0] = 1;
        while(!que.isEmpty()) {
            Pos now = que.remove();
            
            // 동서남북 이동
            for (int i=0; i < 4; i++) {
                int tmpX = now.x + dirX.get(i);
                int tmpY = now.y + dirY.get(i);
                
                if (tmpX < 0 || tmpX >= n || tmpY < 0 || tmpY >= m) // 미로에서 벗어남
                    continue;
                
                // 갈 수 있는 길인가
                // + 방문했던 경우, min 값일때 Que에 넣음
                if (maps[tmpX][tmpY] == 1) {    // 길 있음
                    if (visited[tmpX][tmpY] == -1 
                        || visited[tmpX][tmpY] > visited[now.x][now.y] + 1) {    // 방문한적 없음 or 값이 더 작을 때
                        visited[tmpX][tmpY] = visited[now.x][now.y] + 1;
                        que.add(new Pos(tmpX, tmpY));
                    }
                }
            }
        }
        
        return visited[n-1][m-1];
    }
    
    class Pos{
        int x, y;
        
        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}