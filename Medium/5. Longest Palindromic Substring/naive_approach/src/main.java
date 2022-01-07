public class main {

    public static boolean is_palindrome(String str) {
        int i_low = 0;
        int i_high = str.length() - 1;

        while(i_low < i_high) {
            char c_low = str.charAt(i_low);
            char c_high = str.charAt(i_high);

            if (c_low != c_high) {
                return false;
            }

            //1ms performance gain by using ++X instead of X++
            ++i_low;
            --i_high;
        }
        return true;
    }

    public static String longestPalindrome(String s) {
        if(s == null)
            return "";
        if(s.length() == 1)
            return s;

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
