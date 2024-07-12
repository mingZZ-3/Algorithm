import java.util.*;

class Solution {
    static boolean[] visited;
    static LinkedList<String> result;
    
    public static String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        result = new LinkedList<>();

        dfs(0, "ICN", "ICN", tickets);

        // 알파벳 순서 고려
        Collections.sort(result);
        String[] answer = result.poll().split(" ");

        return answer;
    }

    public static void dfs(int count, String start, String end, String[][] tickets) {
        if (count == tickets.length) { // 도시를 모두 방문 했는지
            result.add(end);
            return;
        }
        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0].equals(start)) { // start와 같고 들리지 않은 공항을 찾고
                visited[i] = true;
                dfs(count + 1, tickets[i][1], end + " " + tickets[i][1], tickets);
                visited[i] = false; // 백트랙킹
            }
        }
    }
}