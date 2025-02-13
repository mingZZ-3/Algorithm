import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
    	// 큰 수가 우선순위가 높은 큐를 선언
        PriorityQueue<Integer> pq = new PriorityQueue(Collections.reverseOrder());
        
        // works의 모든 원소를 큐에 넣음
        for(int i : works)
            pq.add(i);
        
        while(true){
            if(n==0)
                break;
            if(pq.isEmpty())
                break;
            int value = pq.poll();
            n--;
            value -= 1;
            if(value >0)
                pq.add(value);
        }
        
        long answer = 0;
        while(!pq.isEmpty()){ // 큐의 모든 원소를 꺼내며 계산한다.
            int value = pq.poll();
            answer += value * value;
        }
        return answer;
    }
}