public class main {
    public static boolean isPalindrome(int x) {
        String str = String.valueOf(x); //instead of "" + x I did this and it slashes in half (13ms to 7ms) runtime in leet code
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

    public static void main(String[] args) {
        assert(isPalindrome(121));
        assert(isPalindrome(1221));
        assert(!isPalindrome(1231));
        assert(!isPalindrome(12));
        assert(isPalindrome(1));
    }
}
