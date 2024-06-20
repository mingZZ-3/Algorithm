class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        
        char[] nums = number.toCharArray();
        int start = 0;
        
        for(int i = 0; i < nums.length - k; i++){
            char max = '0';
            for(int j = start; j <= i + k; j++){
                if(nums[j] > max){
                    max = nums[j];
                    start=j+1;
                }
            }
            sb.append(Character.toString(max));
        }
        return sb.toString();
    }
}