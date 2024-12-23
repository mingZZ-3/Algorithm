class Solution {
    public int solution(int n) {
        int answer = 0;
        int nCnt = Integer.bitCount(n);
        int bCnt = 0;
        while(true){
            n++;
            bCnt = Integer.bitCount(n);
            if(nCnt == bCnt){
                answer = n;
                break;
            }            
        }
        
        return answer;
    }
}