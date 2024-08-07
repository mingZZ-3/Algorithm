import java.util.*;

class Solution {
    List<Integer> depths; 
    boolean[] visited;
    List<Integer>[] graph;
    int depth;
    
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        int delIdx = 0;
        
        while (delIdx < wires.length) {
            // 초기화
            depths = new ArrayList<>();
            visited = new boolean[n];
            
            graph = new ArrayList[n];
            for (int i=0; i < n; i++) {
                graph[i] = new ArrayList<>();
            }
            
            // 하나의 전력망을 제외한 graph 생성
            for (int i=0; i < wires.length; i++) {
                if (i == delIdx) continue;
                
                int a = wires[i][0] - 1;
                int b = wires[i][1] - 1;
                graph[a].add(b);
                graph[b].add(a);
            }
            
            // 전체 노드를 돌면서 DFS
            for (int i=0; i < n; i++) {
                if (!visited[i]) {
                    depth = 1;
                    DFS(i);
                    depths.add(depth);
                }
            }
            
            answer = Math.min(answer, 
                              Math.abs(depths.get(0) - depths.get(1)));
            delIdx++;
        }
        
        return answer;
    }
    
    void DFS(int i) {
        visited[i] = true;
        for (int next : graph[i]) {
            if (!visited[next]) {
                DFS(next);
                depth += 1;
            }
        }
    }
}
