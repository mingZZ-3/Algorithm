class Solution {
    
    int[] discount = {10, 20, 30, 40};
    int subs = 0;
    int pays = 0;
    
    public int[] solution(int[][] users, int[] emoticons) {
        combination(new int[emoticons.length], 0, users, emoticons);
        
        return new int[]{subs, pays};
    }
    
    public void combination(int[] list, int start, int[][] users, int[] emoticons) {
        if (start == list.length) { // 모든 이모티콘의 할인율이 정해짐
            calc(list, users, emoticons);
            return;
        }
        
        for (int i=0; i<4; i++) {   // 가능한 경우의 수 만들기
            list[start] = discount[i];
            combination(list, start+1, users, emoticons);
        }
    }
    
    public void calc(int[] list, int[][] users, int[] emoticons) {
        int tmpSub = 0;
        int tmpPay = 0;
        
        for (int[] user : users) {
            int sum = 0;
            
            for (int i=0; i<list.length; i++) {
                if (list[i] >= user[0]) {  // 유저의 기준 할인율이상인 경우
                    sum += emoticons[i] - (emoticons[i]*list[i]/100);
                }
            }
            
            if (sum >= user[1]) // 구독
                tmpSub++;
            else
                tmpPay += sum;
        }
        
        if (tmpSub > subs) {  
            // 구독을 더 많이 하는 경우
            subs = tmpSub;
            pays = tmpPay;
            return;
        } else if (tmpSub == subs && tmpPay > pays) {  
            // 구독은 같아도, 수익이 더 많은 경우
            pays = tmpPay;
        }
    }
}