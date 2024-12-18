import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> sets = new HashSet<>();
        
        for (String num : phone_book) {
            sets.add(num);
        }
        
        for (String num : phone_book) {
            for (int i=1; i<num.length(); i++) {
                if (sets.contains(num.substring(0, i)))
                    return false;
            }
        }
        
        return true;
    }
}