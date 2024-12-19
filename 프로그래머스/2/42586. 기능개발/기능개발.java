import java.util.*;

class Solution {
    public int[] solution(int[] progress, int[] speeds) {
        List<Integer> cnts = new ArrayList<>();
        Queue<Integer> que = new ArrayDeque<>();
        
        for (int i=0; i<progress.length; i++) {
            int workday = (100 - progress[i])/speeds[i];
            if ((100 - progress[i])%speeds[i] != 0)
                workday++;
            que.add(workday);
        }
        
        int idx = 0;
        while(!que.isEmpty()) {
            int top = que.remove();
            int cnt = 1;
            
            while (!que.isEmpty() && que.peek() <= top) {
                que.remove();
                cnt++;
            }
            
            cnts.add(cnt);
        }
        
        int[] answer = new int[cnts.size()];
        for (int i=0; i<cnts.size(); i++) {
            answer[i] = cnts.get(i);
        }
        
        return answer;
    }
}