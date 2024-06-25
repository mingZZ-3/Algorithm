class Solution {
    public int solution(String[] babbling) {
        String[] ableList = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        
        for(int i=0; i < babbling.length; i++) {
            for(int j=0; j <ableList.length; j++) {
                babbling[i] = babbling[i].replace(ableList[j], " ");
            }
        }
        
        for(int i=0; i < babbling.length; i++) {
            if (babbling[i].strip().equals(""))
                answer++;
        }
        
        return answer;
    }
}