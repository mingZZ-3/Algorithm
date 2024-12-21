class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int cnt0 = 0;
        int n = 0;
        
        while(true) {
            if (s.equals("1")) break;
            
            int tmpCnt0 = 0;
            for (int i=0; i<s.length(); i++) {
                if (s.charAt(i) == '1') {
                     tmpCnt0++;
                 }
            }
            cnt0 += s.length() - tmpCnt0;
            
            s = Integer.toBinaryString(tmpCnt0);
            
            n++;
        }
        
        answer[0] = n;
        answer[1] = cnt0;
    
        return answer;
    }
}