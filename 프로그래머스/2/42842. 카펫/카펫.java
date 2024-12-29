class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        for (int h = 3; h < 5000; h++) {
            int w = (brown + yellow) / h;
            if (w >= h && yellow == (w-2)*(h-2)) {
                answer[0] = w;
                answer[1] = h;
                break;
            }
        }
        
        return answer;
    }
}