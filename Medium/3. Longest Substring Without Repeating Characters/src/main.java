public class main {

    public static int lengthOfLongestSubstring(String s) {
        if(s.length() == 0)
            return 0;

        int i_low = 0;
        int i_high = 1;

        int max_len = 1;
        int cur_len = 1;

        while(i_high < s.length()) {
            char c_high = s.charAt(i_high);

            //Check if char is not in current segment.
            boolean in_segment = false;
            for(int i = i_low; i < i_high; i++) {
                if(c_high == s.charAt(i)) {
                    in_segment = true;
                    break;
                }
            }
            if(in_segment) {
                //Start new segment.
                i_low ++;
                i_high = i_low + 1;
                cur_len = 1;
            } else {
                i_high++;
                cur_len++;
                max_len = Math.max(max_len, cur_len);
            }
        }
        //We do this again, because the segment can begin from start to end.
        max_len = Math.max(max_len, cur_len);

        return max_len;
    }

    public static void main(String[] args) {
        assert(lengthOfLongestSubstring("abcabcbb") == 3);
        assert(lengthOfLongestSubstring("bbbbb") == 1);
        assert(lengthOfLongestSubstring("pwwkew") == 3);
        assert(lengthOfLongestSubstring("") == 0);
        assert(lengthOfLongestSubstring("au") == 2);
        assert(lengthOfLongestSubstring("dvdf") == 3);
    }
}
