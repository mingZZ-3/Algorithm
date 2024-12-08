import java.util.*;

class Solution {
    public String solution(String s) {
        // List<String> nums = Arrays.stream(s.split(" ")).toList();
        List<String> nums = new ArrayList<>();
        for (String string : s.split(" ")) {
            nums.add(string);
        }
        
        int min_value = Integer.MAX_VALUE;
        int max_value = Integer.MIN_VALUE;

        for (String num : nums) {
            if (Integer.parseInt(num) < min_value) {
                min_value = Integer.parseInt(num);
            }
            if (Integer.parseInt(num) > max_value) {
                max_value = Integer.parseInt(num);
            }
        }

        return min_value + " " + max_value;
    }
}