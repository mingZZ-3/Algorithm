class Solution {
    int cnt = 0;
    public int solution(int[] numbers, int target) {
        Calc(numbers, target, 0, 0);
        return cnt;
    }
    
    public void Calc(int[] numbers, int target, int sum, int idx) {
        if (idx == numbers.length) {
            if (sum == target) cnt++;
            return;
        }
        
        Calc(numbers, target, sum + numbers[idx], idx + 1);
        Calc(numbers, target, sum - numbers[idx], idx + 1);
    }
}