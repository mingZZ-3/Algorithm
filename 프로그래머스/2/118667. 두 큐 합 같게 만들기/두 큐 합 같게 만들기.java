import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int cnt = 0;
        long sum1 = Arrays.stream(queue1).sum();
        long sum2 = Arrays.stream(queue2).sum();
        int max = (queue1.length + queue2.length) * 2;

        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        
        for (int i = 0; i < queue1.length; i++) {
            q1.add(queue1[i]);
        }
        for (int i = 0; i < queue2.length; i++) {
            q2.add(queue2[i]);
        }

        while (true) {
            if (sum1 == sum2)
                break;
            if (cnt > max) {
                cnt = -1;
                break;
            }

            if (sum1 > sum2) {
                int top = q1.poll();
                sum1 -= (long) top;
                q2.add(top);
                sum2 += (long) top;
            } else if (sum2 > sum1) {
                int top = q2.poll();
                sum2 -= (long) top;
                q1.add(top);
                sum1 += (long) top;
            }
            cnt++;
        }

        return cnt;
    }
}