import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Arrays;

public class N_Queen {

    public static void nQueen(int n) {
        HashMap<String, HashSet<Integer>> notAllowed = new HashMap<>();
        notAllowed.put("cols", new HashSet<>());
        notAllowed.put("diag1", new HashSet<>());
        notAllowed.put("diag2", new HashSet<>());

        HashSet<List<Integer>> result = new HashSet<>();

        if (nQueenHelper(n, 0, notAllowed, result)) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(
                        result.contains(Arrays.asList(i, j)) ? 1 : 0);
                    System.out.print(" ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No solution exists");
        }
    }

    public static boolean nQueenHelper(int n, int row,
            HashMap<String, HashSet<Integer>> notAllowed,
            HashSet<List<Integer>> result) {
        if (row == n) {
            return true;
        }
        for (int col = 0; col < n; col++) {
            if (notAllowed.get("cols").contains(col) ||
                    notAllowed.get("diag1").contains(row - col) ||
                    notAllowed.get("diag2").contains(row + col)) {
                continue;
            }

            result.add(Arrays.asList(row, col));
            notAllowed.get("cols").add(col);
            notAllowed.get("diag1").add(row - col);
            notAllowed.get("diag2").add(row + col);

            if (nQueenHelper(n, row + 1, notAllowed, result)) {
                return true;
            }

            result.remove(Arrays.asList(row, col));
            notAllowed.get("cols").remove(col);
            notAllowed.get("diag1").remove(row - col);
            notAllowed.get("diag2").remove(row + col);
        }
        return false;
    }

    public static void main(String[] args) {
        nQueen(1);
    }
}