import java.util.*;

class Solution {
    List<Integer>[] graph;
    List<Node> nodes;
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        graph = new ArrayList[n + 1];
        for (int i=0; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] line : edge) {
            graph[line[0]].add(line[1]);
            graph[line[1]].add(line[0]);
        }
        
        // 최단 거리 저장할 리스트
        nodes = new ArrayList<>();
        for (int i=0; i < n + 1; i++) {
            nodes.add(new Node(i, 99999));
        }
        
        BFS();
        
        // 가장 먼 노드 구하기
        int maxV = -1;
        for (Node node : nodes) {
            if (node.w != 99999)
                maxV = Math.max(maxV, node.w);
        }
        
        for (Node node : nodes) {
            if (node.w == maxV)
                answer++;
        }
        
        return answer;
    }
    
    public void BFS() {    // 1을 기준으로 최단경로 구하기
        Queue<Integer> que = new LinkedList<>();
        que.offer(1);
        nodes.set(1, new Node(1, 0));
        
        while(!que.isEmpty()) {
            int now = que.poll();
            for (Integer next : graph[now]) {
                int weight = nodes.get(now).w + 1;
                
                if (weight < nodes.get(next).w) {
                    nodes.set(next, new Node(next, weight));
                    que.offer(next);
                }
            }
        }
    }
    
    
    class Node {
        int e, w;
        
        public Node(int e, int weight) {
            this.e = e;
            this.w = weight;
        }
    }

}