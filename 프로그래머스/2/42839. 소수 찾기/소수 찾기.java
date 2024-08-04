import java.util.*;

class Solution {
    Set<Integer> candidates = new HashSet<>();
    
    public int solution(String numbers) {
        int answer = 0;
    
        permutation(0, numbers, new boolean[numbers.length()], 0);
        
        System.out.println(candidates.toString());
        for (int num : candidates) {
            if (isPrime(num))
                answer++;
        }
        
        return answer;
    }
    
    public void permutation(int curr, String numbers, boolean[] visited, int digit) {
        if (digit == numbers.length()) {
            return;
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (visited[i]) continue;
            
            int newValue = curr + (int)((numbers.charAt(i) - '0')*Math.pow(10, digit));
            candidates.add(newValue);
            
            visited[i] = true;
            permutation(newValue, numbers, visited, digit + 1);
            visited[i] = false;
        }
    }
    
    public boolean isPrime(int n) {
        if (n < 2) return false;
        
        for (int i=2; i*i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}