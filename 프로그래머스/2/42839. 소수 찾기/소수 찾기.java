import java.util.*;

class Solution {
    Set<Integer> nums = new HashSet<>();
    
    public int solution(String numbers) {
        permutation(0, numbers, 0, new boolean[numbers.length()]);
        
        int answer = 0;
        for (int num : nums) {
            if (isPrime(num)) answer++;
        }
        
        return answer;
    }
    
    public boolean isPrime(int n) {
        if (n < 2) return false;
        
        for (int i=2; i*i<=n; i++) {
            if (n % i == 0) return false;
        }
        
        return true;
    }
    
    public void permutation(int curr, String numbers, int digit, boolean[] visited) {
        if (digit == numbers.length()) return;
        
        for (int i=0; i<numbers.length(); i++) {
            if (visited[i]) continue;
            
            int newValue = curr + (int) ((numbers.charAt(i) - '0')*Math.pow(10, digit));
            nums.add(newValue);
            
            visited[i] = true;
            permutation(newValue, numbers, digit+1, visited);
            visited[i] = false;
        }
    }
}