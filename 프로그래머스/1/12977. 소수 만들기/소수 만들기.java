import java.util.*;

class Solution {
    List<Set<Integer>> combis = new ArrayList<>();
    
    public int solution(int[] nums) {
        int answer = 0;

        combi(nums, 0, new HashSet<>());

        
        for (Set<Integer> combi : combis) {
            int sum = 0;
            for (Integer n : combi) sum += n;
            if (isPrime(sum)) answer++;
        }

        return answer;
    }
    
    public void combi(int[] nums, int start, Set<Integer> curr) {
        if (curr.size() == 3) {
            combis.add(new HashSet<>(curr));
            return;
        }
        
        for (int i=start; i<nums.length; i++) {
            curr.add(nums[i]);
            combi(nums, i+1, curr);
            curr.remove(nums[i]);
        }
    }
    
    public boolean isPrime(int num) {
        if (num < 2) return false;
        
        for (int i=2; i*i<= num; i++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }
}