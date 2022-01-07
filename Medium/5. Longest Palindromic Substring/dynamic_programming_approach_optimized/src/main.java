import java.util.ArrayList;
import java.util.List;

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
        for(int i = 0; i < rows; i++) {
            matrix[i][i] = true;
        }

        //Set the diagonal one above the primary diagonal (with increased row, and increased col)
        //Complexity: O(n)
        int longest_palindrome_index_low = 0;
        int longest_palindrome_index_high = 0;

        for(int i = 0; i < rows - 1; i++) {
            boolean is_palindrome = (s.charAt(i) == s.charAt(i+1));
            if(is_palindrome) {
                matrix[i][i+1] = true;
                longest_palindrome_index_low = i;
                longest_palindrome_index_high = i+1;
            } else {
                matrix[i][i+1] = false;
            }
        }

        //This is the critical part where instead of checking each substring O(n) is palindrome,
        //we check the table instead.
        //Complexity: O(n^2)

        int longest_palindrome_length = 1;
        for(int diag_num = 2; diag_num < s.length(); diag_num++) {
            for(int row = 0; row < rows - 1; row++) {
                if(s.charAt(row) == s.charAt(diag_num)) {
                    if(matrix[row + 1][diag_num - 1]) {
                        //'a' == 'a' and 'bab' is palindrome so 'ababa' is also palindrome!
                        matrix[row][diag_num] = true;
                        if((diag_num - row) > longest_palindrome_length) {
                            longest_palindrome_index_low = row;
                            longest_palindrome_index_high = diag_num;
                            longest_palindrome_length = diag_num - row;
                        }
                    }
                }
            }
        }

        //Print matrix
//        System.out.println("\nString: '" + s + "'");
//        for(int col = 0; col < cols; col++) {
//            System.out.print("\t" + s.charAt(col) + "\t");
//        }
//        System.out.println();
//        for(int col = 0; col < cols; col++) {
//            System.out.print("\t" + col + "\t");
//        }
//        System.out.println();
//        for(int row = 0; row < rows; row++) {
//            System.out.print(s.charAt(row) + " " + row + "\t");
//            for(int col = 0; col < cols; col++) {
//                System.out.print(matrix[row][col] + "\t");
//            }
//            System.out.println();
//        }

        String longest_palindrome = s.substring(longest_palindrome_index_low, longest_palindrome_index_high + 1);

        //Print matrix
//        System.out.println("\nString: '" + s + "'");
//        for(int col = 0; col < cols; col++) {
//            System.out.print("\t" + s.charAt(col) + "\t");
//        }
//        System.out.println();
//        for(int col = 0; col < cols; col++) {
//            System.out.print("\t" + col + "\t");
//        }
//        System.out.println();
//        for(int row = 0; row < rows; row++) {
//            System.out.print(s.charAt(row) + " " + row + "\t");
//            for(int col = 0; col < cols; col++) {
//                System.out.print(matrix[row][col] + "\t");
//            }
//            System.out.println();
//        }

        //It will never reach this end of the function.
        //Because the matrix contains at least 1 palindrome (which can be of length 1, meaning it is on the primary diagonal)
        return longest_palindrome;
    }

    public static void main(String[] args) {
        {
            List<String> list = new ArrayList<>();
            list.add("bab");
            list.add("aba");

            String res = longestPalindrome("babad");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("bb");

            String res = longestPalindrome("cbbd");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("a");

            String res = longestPalindrome("a");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("a");

            String res = longestPalindrome("ac");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("ccc");

            String res = longestPalindrome("ccc");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("bab");
            list.add("aba");

            String res = longestPalindrome("babad");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("cc");

            String res = longestPalindrome("ccd");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("cc");

            String res = longestPalindrome("dcc");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("gykrkyg");

            String res = longestPalindrome("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir");
            assert (list.contains(res));
        }

        {
            List<String> list = new ArrayList<>();
            list.add("aaaa");

            String res = longestPalindrome("aaaa");
            assert (list.contains(res));
        }
    }
}
