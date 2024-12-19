class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] result = {0, sequence.length};
        
        int total = 0;
        int start = 0;
        
        for (int end=0; end < sequence.length; end++) {
            total += sequence[end];
            
            while (total > k) {
                total -= sequence[start];
                start++;
            }
            
            if (total == k) {
                if ((end - start) < (result[1] - result[0])) {
                    result[0] = start;
                    result[1] = end;
                }
            }
        }
        
        return result;
    }
}