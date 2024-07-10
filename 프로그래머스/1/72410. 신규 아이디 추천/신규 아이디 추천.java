class Solution {
    public String solution(String new_id) {
        StringBuilder sb = new StringBuilder();

        // 소문자 대치
        new_id = new_id.toLowerCase();

        // 사용할 수 없는 문자 걸러내기
        for (char c : new_id.toCharArray()) {
            if (c >= 'a' && c <= 'z' || c >= '0' && c <= '9' || c == '-' || c == '_' || c == '.') {
                sb.append(c);
            }
        }
        new_id = sb.toString();

        // 연속되는 마침표 제거
        sb = new StringBuilder();
        boolean flag = false;
        for (char c : new_id.toCharArray()) {
            if (c == '.') {
                if (!flag) {
                    sb.append(c);
                    flag = true;
                }
            } else {
                sb.append(c);
                flag = false;
            }
        }
        new_id = sb.toString();

        // 처음과 끝의 마침표 제거
        if (new_id.startsWith(".")) {
            new_id = new_id.substring(1);
        }
        if (new_id.endsWith(".")) {
            new_id = new_id.substring(0, new_id.length() - 1);
        }

        // 빈배열일때 'a'
        if (new_id.isEmpty()) {
            new_id = "a";
        }

        // 최대 길이 15개, 마침표 최종 확인
        if (new_id.length() > 15) {
            new_id = new_id.substring(0, 15);
            if (new_id.endsWith(".")) {
                new_id = new_id.substring(0, new_id.length() - 1);
            }
        }

        // len = 2개 이하인 경우, 마지막 문자 반복해서 len = 3까지 채우기
        sb = new StringBuilder(new_id);
        if (new_id.length() < 3) {
            for (int i = 0; i < 3 - new_id.length(); i++) {
                sb.append(new_id.charAt(new_id.length() - 1));
            }
        }

        return sb.toString();
    }
}