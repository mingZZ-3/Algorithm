import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Queue<Node> que = new ArrayDeque<>();
        boolean[] visited = new boolean[words.length];
        
        que.add(new Node(begin, 0));
        while(!que.isEmpty()) {
            Node node = que.remove();
            if (node.word.equals(target)) return node.cnt;
            
            for (int i=0; i<words.length; i++) {
                if (!visited[i] && isOneDiff(node.word, words[i])) {
                    visited[i] = true;
                    que.add(new Node(words[i], node.cnt + 1));
                }
            }
        }
        
        return 0;
    }
    
    public boolean isOneDiff(String a, String b) {
        int diff = 0;
        
        for (int i=0; i<a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) diff++;
        }
        
        return diff == 1? true : false;
    }
    
    class Node {
        int cnt;
        String word;
        
        public Node(String word, int cnt) {
            this.cnt = cnt;
            this.word = word;
        }
    }
}