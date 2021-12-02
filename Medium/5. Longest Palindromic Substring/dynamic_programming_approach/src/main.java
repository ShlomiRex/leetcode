public class main {
    public static String longestPalindrome(String s) {
        if(s == null)
            return "";

        if(s.length() == 1)
            return s;

        if(s.length() == 2) {
            if(s.charAt(0) == s.charAt(1))
                return s;
            return ""+s.charAt(0);
        }

        //Create 2D matrix, that each cell is (i, j) so that i, j represent the indexes of the substrings
        int rows = s.length();
        int cols = s.length();

        //Create 'true' or 'false' matrix for each substring
        boolean[][] matrix = new boolean[rows][cols];

        //Set the primary diagonal
        //Complexity: O(n)
        for(int i = 0; i < matrix.length; i++) {
            matrix[i][i] = true;
        }

        //Set the diagonal one above the primary diagonal (with increased row, and increased col)
        //Complexity: O(n)
        for(int i = 0; i < rows - 1; i++) {
            char first_char = s.charAt(i);
            char second_char = s.charAt(i+1);

            boolean is_palindrome = (first_char == second_char);
            matrix[i][i+1] = is_palindrome;
        }

        //This is the critical part where instead of checking each substring O(n) is palindrome,
        //we check the table instead.
        //Complexity: O(n^2)
        for(int diag_num = 2; diag_num < s.length(); diag_num++) {
            int col = diag_num;

            for(int row = 0; row < rows - 1; row++) {
                //(2, 5) = (5, 2)
                //We find lowest and highest whichever from row or col.
                //'diag_num' is always greater (and never equal to) row.

                //Example: 'ababa' => 'bab' is palindrome and 'a' is left most char
                //and 'a' is right most char

                char left_most_char = s.charAt(row);
                char right_most_char = s.charAt(col);
                boolean is_inner_palindrome = matrix[row + 1][col - 1];

                if(left_most_char == right_most_char && is_inner_palindrome) {
                    //'a' == 'a' and 'bab' is palindrome so 'ababa' is also palindrome!
                    matrix[row][col] = true;
                }
            }
        }

        //Print matrix
        System.out.println("\nString: '" + s + "'");
        for(int col = 0; col < cols; col++) {
            System.out.print("\t" + s.charAt(col) + "\t");
        }
        System.out.println();
        for(int col = 0; col < cols; col++) {
            System.out.print("\t" + col + "\t");
        }
        System.out.println();
        for(int row = 0; row < rows; row++) {
            System.out.print(s.charAt(row) + " " + row + "\t");
            for(int col = 0; col < cols; col++) {
                System.out.print(matrix[row][col] + "\t");
            }
            System.out.println();
        }

        //Check the top-right corner of the matrix for palindrome
        if(matrix[0][cols-1]) {
            return s.substring(0, s.length());
        }

        //Find the longest palindrome (we could do it in previous loop but this code is not optimized for readability)
        for(int diag_num = s.length() - 2; diag_num >= 0; diag_num--) {
            int col = diag_num;
            for(int row = 0; row < rows -1; row++) {
                boolean is_palindrome = matrix[row][diag_num];
                if(is_palindrome) {
                    //We found the longest, first, palindrome.

                    //'diag_num' is always greater than 'row'. So the index starts at 'row' and ends at 'diag_num'.
                    String palindrome = s.substring(row, col + 1);
                    return palindrome; //This function always return at this point.
                }
                col ++;
            }
        }

        //It will never reach this end of the function.
        //Because the matrix contains at least 1 palindrome (which can be of length 1, meaning it is on the primary diagonal)
        return "";
    }

    public static void main(String[] args) {
        assert("aba".equals(longestPalindrome("babad")));
        assert("bb".equals(longestPalindrome("cbbd")));
        assert("a".equals(longestPalindrome("a")));
        assert("a".equals(longestPalindrome("ac")));
        assert("ccc".equals(longestPalindrome("ccc")));
        assert("aba".equals(longestPalindrome("babad")));
        assert("cc".equals(longestPalindrome("ccd")));
        assert("cc".equals(longestPalindrome("dcc")));
    }
}
