import java.util.*;

class Solution {
    int[] dirX = {0, 0, 1, -1};
    int[] dirY = {1, -1, 0, 0};
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
                
        for (int i = 0; i < answer.length; i++) {
            if (check(places[i])) answer[i] = 1;
        }
        return answer;
    }
    
    boolean check(String[] place) {
        for (int i=0; i < 5; i++) {
                for (int j=0; j < 5; j++) {
                    if (place[i].charAt(j) == 'P')
                        if (!BFS(place, i, j)) {// 거리두기 실패
                            return false;
                }
            }
        }
        return true;
    }
    
    // 맨해튼값 2 이내에 P가 없으면 true.
    public boolean BFS(String[] graph, int x, int y) {
        boolean[][] visited = new boolean[5][5];
        Queue<int[]> que = new ArrayDeque<>();
        
        que.add(new int[]{x, y, 0});
        visited[x][y] = true;
        while(!que.isEmpty()) {
            int[] now = que.remove();
            
            // 해당 값의 상하좌우는 맨해튼값이 2를 넘어가서 검사할 필요가 없음.
            if (now[2] >= 2) continue;  
            
            for (int i=0; i < 4; i++) {
                int nx = now[0] + dirX[i];
                int ny = now[1] + dirY[i];
                
                // 범위를 벗어나지 않고, X가 아닌 경우 
                if (inRange(nx, ny) && graph[nx].charAt(ny) != 'X') {
                    if (!visited[nx][ny]) {
                        if (graph[nx].charAt(ny) == 'P') return false;

                        que.add(new int[]{nx, ny, now[2] + 1});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
        return true;
    }
    
    boolean inRange(int r, int c) {
        return (r >= 0) && (r < 5) && (c >= 0) && (c < 5);
    }
}