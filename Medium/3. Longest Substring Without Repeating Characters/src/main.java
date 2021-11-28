public class main {

    public static int lengthOfLongestSubstring(String s) {
        if(s.length() == 0)
            return 0;

        int i_low = 0;
        int i_high = 0;

        int max_len = 1;
        int cur_len = 1;

        while(i_high < s.length() - 1) {
            i_high ++;
            char c_high = s.charAt(i_high);

            boolean is_added = true;
            for(int i = i_low; i < i_high; i++) {
                if(c_high == s.charAt(i)) {
                    //start new segment
                    max_len = Math.max(max_len, i_high - i_low);

                    i_low ++;
                    i_high = i_low + 1;

                    is_added = false;
                    cur_len = 1;
                    break;
                }
            }
            if(is_added) {
                cur_len += 1;
            }
        }

        max_len = Math.max(max_len, cur_len);

        return max_len;
    }

    public static void main(String[] args) {
//        assert(lengthOfLongestSubstring("abcabcbb") == 3);
//        assert(lengthOfLongestSubstring("bbbbb") == 1);
//        assert(lengthOfLongestSubstring("pwwkew") == 3);
//        assert(lengthOfLongestSubstring("") == 0);
//        assert(lengthOfLongestSubstring("au") == 2);
        assert(lengthOfLongestSubstring("dvdf") == 3);
    }
}
