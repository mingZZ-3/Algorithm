import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
       int[] result = new int[prices.length];
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < prices.length; i++) {
            q.add(prices[i]);
        }
        
        int idx = 0;
        while (q.peek() != null) {
            int price = q.poll();
            result[idx] = 0;

            for (Integer nextPrice : q) {
                result[idx]++;
                if (price > nextPrice) {
                    break;
                }
            }

            idx++;
        }

        return result;
    }
}