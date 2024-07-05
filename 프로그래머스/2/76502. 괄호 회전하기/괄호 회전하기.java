import java.util.*;

class Solution {
    public int solution(String s) {
        int cnt = 0, check = 0, rounding = 0;
        Queue<Character> q = new ArrayDeque<>();
        for (int i = 0; i <s.length(); i++) {
            char c = s.charAt(i);
            q.add(c);
            if (c =='(' || c =='{' || c =='[') {
                check += 1;
            } else {
                check -= 1;
            }
        }
        if (check != 0) {  // 양끝의 개수가 맞지앉음.
            return 0;
        }

        while (true) {
            Stack<Character> stack = new Stack<>();
            if (rounding == s.length() - 1)
                break;

            for (char ch : q) {
                if (ch == '(' || ch == '{' || ch == '[') {
                    stack.push(ch);
                } else if (stack.isEmpty()) {
                    cnt--;
                    break;
                } else if (ch == ')' && stack.peek() == '(') {
                    stack.pop();
                } else if (ch == '}' && stack.peek() == '{') {
                    stack.pop();
                } else if (ch == ']' && stack.peek() == '[') {
                    stack.pop();
                }
            }

            if (stack.isEmpty())
                cnt++;

            char a = q.remove();
            q.add(a);
            rounding++;
        }
        return cnt;
    }
}