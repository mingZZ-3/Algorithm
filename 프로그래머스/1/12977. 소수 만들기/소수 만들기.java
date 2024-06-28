import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        boolean[] primelist = isPrimeList(2997);

        for(int i = 0; i < nums.length - 2; i++) {
            for (int startp = i + 1; startp < nums.length - 1; startp++) {
                int endp = startp + 1;
                while (endp < nums.length){
                    int sum = nums[i] + nums[startp] + nums[endp];
                    if (primelist[sum]) answer++;
                    endp++;
                }
            }
        }

        return answer;
    }
    
    private boolean[] isPrimeList(int max) {
        boolean[] isPrime = new boolean[max + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i <= max; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= max; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        
        return isPrime;
    }
}