import java.util.*;

class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        
        // graph 초기화
        int[][] graph = new int[n+1][n+1];
        for (int[] fare : fares) {
            graph[fare[0]][fare[1]] = fare[2];
            graph[fare[1]][fare[0]] = fare[2];
        }
        
        // dist 초기화 - s, a, b 3개의 노드에서 모든 노드까지 도달하는 최소 비용
        int[][] dist = new int[3][n+1];
        for (int[] d : dist) {
            Arrays.fill(d, Integer.MAX_VALUE);
        }
        
        // 다익스트라
        Queue<int[]> q = new PriorityQueue<>((e1, e2) -> e1[1] - e2[1]);
        final int[] start = {s, a, b};
        for (int j=0; j<3; j++) {
            int[] d = dist[j];
            q.add(new int[]{start[j], 0}); // s, a, b를 시작점으로 최저 금액 계산
            d[start[j]] = 0;
            while(!q.isEmpty()) {
                int[] now = q.remove();
                
                for (int i=1; i <= n; i++) {
                    if (graph[now[0]][i] == 0) continue; // 길이 없음
                    if (d[i] > now[1] + graph[now[0]][i]) {
                        // 비용이 더 적음
                        d[i] = now[1] + graph[now[0]][i];
                        q.add(new int[]{i, now[1] + graph[now[0]][i]});
                    }
                }
            }
        }
        
        // 최소비용 구하기
        int minCost = Integer.MAX_VALUE;
        for (int i=1; i<=n; i++) {
            int sum = 0;
            for (int[] d : dist) {
                sum += d[i];
            }
            minCost = Math.min(minCost, sum);
        }
        
        return minCost;
    }
}