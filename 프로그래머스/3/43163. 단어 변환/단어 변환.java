import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Queue<Node> que = new ArrayDeque<>();
        boolean[] visited = new boolean[words.length];
        
        que.add(new Node(0, begin));
        
        while(!que.isEmpty()) {
            Node node  = que.remove();
            if (node.word.equals(target)) return node.cnt;
            
            for (int i=0; i < words.length; i++) {
                if (!visited[i] && isOneDiff(node.word, words[i])) {
                    visited[i] = true;
                    que.add(new Node(node.cnt + 1, words[i]));
                }
            }
        }
        
        return 0;
    }
    
    public boolean isOneDiff(String a, String target) {
        int diffCount = 0;
        
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != target.charAt(i)) diffCount++;
        }
        return diffCount == 1? true : false;
    }
    
    class Node{
        int cnt;
        String word;
        
        public Node(int cnt, String word) {
            this.cnt = cnt;
            this.word = word;
        }
    }
}
