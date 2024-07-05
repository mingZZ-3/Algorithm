import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> result = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < progresses.length; i++) {
            int workday = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] != 0) {
                workday++;
            }
            queue.add(workday);
        }

        int top = queue.poll();
        int cnt = 1;
        while (!queue.isEmpty()) {
            int nextwork = queue.peek();

            if (nextwork > top) {
                result.add(cnt);

                cnt = 1;
                top = queue.poll();
            
            } else {
                queue.poll();
                cnt++;
            }
        }
        result.add(cnt);

        int[] res = result.stream().mapToInt(i->i).toArray();

        return res;
    }
}