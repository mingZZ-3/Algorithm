import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int idx = 0;
        int answer = 0;
        
        for (int i = people.length - 1; i >= idx;i--) {
            if(people[idx] + people[i] <= limit) {
                answer++;
                idx++;
            } else {
                answer++;
            }
        }


        return answer;
    }
}