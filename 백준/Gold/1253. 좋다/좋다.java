import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        int cnt = 0;
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        for (int i = 0; i < N; i++) {
            int startP = 0, endP = N-1;

            while(true) {
                if(startP == i) startP++;
                else if(endP == i) endP--;
                
                 if(startP >= endP) break;

                long sum = nums[startP] + nums[endP];
                if (sum == nums[i]) {
                    cnt++;
                    break;
                } else if (sum < nums[i]) {
                    startP++;
                } else {
                    endP--;
                }
            }
        }
        System.out.println(cnt);
    }
}