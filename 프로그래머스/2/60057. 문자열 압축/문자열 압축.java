import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(String s) {
        int result = s.length();
        
        for (int l=1; l <= s.length()/2; l++) {
            List<String> words = new ArrayList<>();
            for (int i=0; i<s.length(); i += l) {
                words.add(s.substring(i, Math.min(i+l, s.length())));
            }
            
            Deque<Entry> stack = new ArrayDeque<>();
            stack.push(new Entry(words.get(0), 1));
            for (String w : words.subList(1, words.size())) {
                if (stack.peek().word.equals(w)) {
                    Entry top = stack.pop();
                    stack.push(new Entry(top.word, top.cnt+1));
                } else {
                    stack.push(new Entry(w, 1));
                }
            }
            
            String compressed = stack.stream().map(Entry::toString).collect(Collectors.joining());
            result = Math.min(compressed.length(), result);
        }
        
        return result;
    }
    
    class Entry {
        String word;
        int cnt;
        
        public Entry(String w, int c) {
            this.word = w;
            this.cnt = c;
        }
        
        @Override
        public String toString() {
            return (cnt == 1) ? word : cnt + word; 
        }
    }
}