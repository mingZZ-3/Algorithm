class Solution {
    static int cnt = 0;
    static int target;
    
    public int solution(int[] numbers, int t) {
        target = t;
        dfs(numbers, 0, 0);
        return cnt;
    }
    
    public void dfs(int[] numbers, int depth, int result) {
        if (depth == numbers.length) {
            if (result == target) {
                cnt++;
            }
            return;
        }

        int tmp1 = result - numbers[depth];
        int tmp2 = result + numbers[depth];
        
        dfs(numbers, depth+1, tmp1);
        dfs(numbers, depth+1, tmp2);
    }
}