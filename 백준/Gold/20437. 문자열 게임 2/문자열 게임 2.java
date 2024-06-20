import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 게임 수만큼 돌리기
        for (int i = 0; i < N; i++) {
            String game = br.readLine();
            int k = Integer.parseInt(br.readLine());
            int min_cnt = 10001, max_cnt = -1;
            
            if (game.length() <= 0) {
                System.out.println("-1");
            }
            
            if (k == 1) {
                System.out.println("1 1");
                continue;
            }

            // 알파벳 수 구하기
            int[] alphaList = new int[26];
            for (int j = 0; j < game.length(); j++) {
                alphaList[game.charAt(j) - 'a']++;
            }

            for (int j = 0; j < game.length(); j++) { // startP
                // 알파벳 개수가 k이하면 패스
                if (alphaList[game.charAt(j) - 'a'] < k)
                    continue;

                // 이상인 경우, min max 계산 돌리기
                int cnt = 1;
                for (int q = j + 1; q < game.length(); q++) { // endP
                    // 같은 문자면 cnt++ --> cnt==k면 min, max확인
                    if (game.charAt(j) == game.charAt(q))
                        cnt++;

                    if (cnt == k) {
                        min_cnt = Math.min(min_cnt, q - j + 1);
                        max_cnt = Math.max(max_cnt, q - j + 1);
                        break;
                    }
                }
            }

            if (min_cnt == 10001 || max_cnt == -1) {
                System.out.println(-1);
            } else {
                System.out.println(min_cnt + " " + max_cnt);
            }
        }
    }
}