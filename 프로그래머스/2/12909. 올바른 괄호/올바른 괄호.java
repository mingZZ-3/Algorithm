import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(s.charAt(i));
            }
            else {
                if (!stack.empty() && stack.peek() == '(') {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }
        return stack.empty() ? true : false;
    }
}