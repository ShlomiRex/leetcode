import org.junit.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

import static org.junit.Assert.assertEquals;

public class main {
    public static int romanToInt(String s) {
        int result = 0;

        HashMap<Character, Integer> symbols = new HashMap<>()
        {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};

        if(s.length() == 1)
            return symbols.get(s.charAt(0));
        else
            result += symbols.get(s.charAt(0));

        int last_symbol_value = symbols.get(s.charAt(0));

        for(int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            int symbol_value = symbols.get(c);

            if(last_symbol_value >= symbol_value) {
                //If next character is placed after another of equal or greater value, adds its value
                result += symbol_value;
            }
            else {
                //Else, a symbol is placed before one of greater value substracts its value
                result += (symbol_value - last_symbol_value);
                result -= last_symbol_value;
            }

            last_symbol_value = symbol_value;
        }

        return result;
    }

    @Test
    public void testSimple() {
        assertEquals(1, romanToInt("I"));
        assertEquals(3, romanToInt("III"));
        assertEquals(5, romanToInt("V"));
        assertEquals(3000, romanToInt("MMM"));
    }

    @Test
    public void testAscending() {
        assertEquals(4, romanToInt("IV"));
    }

    @Test
    public void testDecending() {
        assertEquals(6, romanToInt("VI"));
        assertEquals(7, romanToInt("VII"));
        assertEquals(60, romanToInt("LX"));
    }

    @Test
    public void test1000Numbers() throws FileNotFoundException {
        Scanner s = new Scanner(new File("test/romains_1_to_1000.txt"));
        long number = 0;
        while(s.hasNextLine()) {
            String line = s.nextLine();
            number++;

            assertEquals(number, romanToInt(line));
        }
    }
}
