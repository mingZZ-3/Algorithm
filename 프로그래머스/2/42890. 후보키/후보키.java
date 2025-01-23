import java.util.*;

class Solution {
    public int solution(String[][] relation) {
        int colSize = relation[0].length;  // 칼럼의 개수
        
        List<Set<Integer>> candidates = new ArrayList<>();
        
        // 1 ~ n의 길이의 조합
        for (int size = 1; size <= colSize; size++) {
		        // size 길이의 조합 생성
            List<Set<Integer>> combinations = generateCombinations(colSize, size);
            for (Set<Integer> comb : combinations) {
		            // 유일성, 최소성 조건 확인
                if (checkUnique(comb, relation) && checkMin(comb, candidates))
                    candidates.add(comb);
            }
        }
        
        return candidates.size();
    }
    
    // 유일성 검사
    boolean checkUnique(Set<Integer> cols, String[][] relation) {
        int rowSize = relation.length;
        Set<String> rowSet = new HashSet<>();
        
        for (String[] row : relation) {
            StringBuilder rowStr = new StringBuilder();
            for (int col : cols) {
                rowStr.append(row[col]);
            }
            rowSet.add(rowStr.toString());
        }
        
        if (rowSet.size() == rowSize)
            return true;
        return false;
    }
    
    // 최소성 검사
    boolean checkMin(Set<Integer> comb, List<Set<Integer>> candidates) {
        for (Set<Integer> key : candidates) {
            if (comb.containsAll(key))
                return false;
        }
        return true;
    }
    
    // r 길이의 조합 생성
    List<Set<Integer>> generateCombinations(int colSize, int r) {
        List<Set<Integer>> combinations = new ArrayList<>();
        generateCombinationsHelper(new HashSet<>(), 0, colSize, r, combinations);
        return combinations;
    }
    
    void generateCombinationsHelper(Set<Integer> curr, int start, int colSize, int r, List<Set<Integer>> result) {
        if (curr.size() == r) {
            result.add(new HashSet<>(curr));
            return;
        }
        
        for (int i=start; i < colSize; i++) {
            curr.add(i);
            generateCombinationsHelper(curr, i+1, colSize, r, result);
            curr.remove(i);
        }
    }
}