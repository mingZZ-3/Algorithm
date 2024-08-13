import java.util.*;

class Solution {
    int[] distX = {0, 0, 1, -1};
    int[] distY = {1, -1, 0, 0};
    int sl = 0, le = 0;
    int n , m;
    boolean[][] visited;
    char[][] map;
    
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        map = new char[n][m];
        Node s = null, l = null, e = null;
        
        for (int i=0; i < maps.length; i++) {
            map[i] = maps[i].toCharArray();
            for (int j=0; j <maps[0].length(); j++) {
                if (maps[i].charAt(j) == 'S')
                    s = new Node(i, j, 0); 
                else if (maps[i].charAt(j) == 'L')
                    l = new Node(i, j, 0);
                else if (maps[i].charAt(j) == 'E')
                    e = new Node(i, j, 0);
            }
        }
        
        // S -> L
        sl = BFS(s, l);
        if (sl == -1) return -1;
        
        // L -> E
        le = BFS(l, e);
        if (le == -1) return -1;
        
        return sl + le;
    }
    
    int BFS(Node start, Node target) {
        visited = new boolean[n][m];
        Queue<Node> que = new ArrayDeque<>();
        que.add(start);
        
        visited[start.x][start.y] = true;
        while(!que.isEmpty()) {
            Node now = que.remove();
            
            // 현재 위치에서 상하좌우로 이동
            for (int i=0; i < 4; i++) {
                int nx = now.x + distX[i];
                int ny = now.y + distY[i];
                
                if (InRange(nx, ny) 
                    && !visited[nx][ny] && map[nx][ny] != 'X') {
                    if (nx == target.x && ny == target.y) // 목적지에 도착
                        return now.time + 1;
                    
                    visited[nx][ny] = true;
                    que.add(new Node(nx, ny, now.time + 1));
                }
            }
        }
        return -1;
    }
    
    boolean InRange(int x, int y) {
        return (x >= 0) && (x < n) && (y >= 0) && (y < m);
    }
    
    class Node {
        int x, y, time;
        
        Node(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }
}