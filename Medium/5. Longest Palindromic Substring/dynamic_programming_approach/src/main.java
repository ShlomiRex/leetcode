public class main {

    public static String longestPalindrome(String s) {
        if(s == null)
            return "";
        if(s.length() == 1)
            return s;

        //Create 2D matrix, that each cell is (i, j) so that i, j represent the indexes of the substrings
        int rows = s.length();
        int cols = s.length();

        //Create 'true' or 'false' matrix for each substring
        boolean[][] matrix = new boolean[rows][cols];

        int i_low = 0;
        String longest_poly = "";

        while(i_low < s.length() - 1) {
            for(int i_high = i_low; i_high < s.length(); i_high++) {
                String substr = s.substring(i_low, i_high + 1);
                if(substr.length() > longest_poly.length() && is_palindrome(substr)) {
                    longest_poly = substr;
                }
            }
            ++i_low;
        }

        return longest_poly;
    }

    public static void main(String[] args) {
        assert("bab".equals(longestPalindrome("babad")));
        assert("bb".equals(longestPalindrome("cbbd")));
        assert("a".equals(longestPalindrome("a")));
        assert("a".equals(longestPalindrome("ac")));
    }
}
