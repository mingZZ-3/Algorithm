class Solution {
    public long solution(int n) {
        long[] dp = new long[2001];
           
        // 0-0, 1-1, 2-2, 3-3, 4-5
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i=3; i<n+1; i++) {
            dp[i] = dp[i-1] + dp[i-2];
            dp[i] %= 1234567;
        }
        
        return dp[n];
    }

    
}