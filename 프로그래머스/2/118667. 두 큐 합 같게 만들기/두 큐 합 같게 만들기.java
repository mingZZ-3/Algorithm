import java.util.*;

class Solution {
    public int solution(int[] que1, int[] que2) {
        int cnt = 0;
        long sum1 = Arrays.stream(que1).sum();
        long sum2 = Arrays.stream(que2).sum();
        int max = que1.length * 3;
        
        if ((sum1 + sum2) % 2 != 0) return -1;
        
        Queue<Integer> q1 = new ArrayDeque<>();
        for (int n : que1) {
            q1.add(n);
        }
        Queue<Integer> q2 = new ArrayDeque<>();
        for (int n : que2) {
            q2.add(n);
        }
        
        while(true) {
            if (sum1 == sum2) break;
            
            if (cnt > max) {
                cnt = -1;
                break;
            }
            
            if (sum1 > sum2) {
                int num = q1.poll();
                sum1 -= num;
                q2.add(num);
                sum2 += num;
            } else {
                int num = q2.poll();
                sum2 -= num;
                q1.add(num);
                sum1 += num;
            }
            cnt++;
        }
        
        return cnt;
    }
}