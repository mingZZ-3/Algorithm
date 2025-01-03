import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0,0};
        List<String> list = new ArrayList<>();
        list.add(words[0]);
                
        for (int i=1; i<words.length; i++) {
            if (list.contains(words[i]) || !correctLetter(list.get(list.size() - 1), words[i])) {
                answer[0] = i%n + 1;
                answer[1] = i/n + 1;
                break;
            }
            list.add(words[i]);
        }
         

        return answer;
    }
    
    public boolean correctLetter(String last, String newL) {
        if (last.charAt(last.length()-1) == newL.charAt(0))
            return true;
        else
            return false;
    }
}