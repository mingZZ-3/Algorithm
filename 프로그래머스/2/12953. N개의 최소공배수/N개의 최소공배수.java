import java.util.*;

class Solution {
    public int solution(int[] arr) {
        if (arr.length == 1) return arr[0];
        
        Arrays.sort(arr);
        
        for (int i=0; i < arr.length-1; i++) {
            int n = calc(arr[i], arr[i+1]);
            arr[i+1] = (arr[i] * arr[i+1]) / n;
        }
        
        
        return arr[arr.length-1];
    }
    
    public int calc(int a, int b) { // 최대 공약수 
        int c = a % b;
        if (c == 0) return b;
        else return calc(b, c);
    }
}