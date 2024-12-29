import java.util.*;

class Solution {
    int[] fibos;
    
    public int solution(int n) {
        fibos = new int[100001];
        Arrays.fill(fibos, -1);
        fibos[0] = 0;
        fibos[1] = 1;
        
        return fibo(n);
    }
    
    public int fibo(int n) {
        if (fibos[n] == -1) {
            fibos[n] = (fibo(n-1) + fibo(n-2)) % 1234567;
        }
        
        return fibos[n];
    }
}