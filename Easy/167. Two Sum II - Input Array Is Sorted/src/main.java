public class main {

    public static int[] twoSum(int[] numbers, int target) {
        int i_low = 0;
        int i_high = numbers.length - 1;
        int[] res = new int[2];

        while (i_low != i_high) {
            int sum = numbers[i_low] + numbers[i_high];
            if (sum == target) {
                res[0] = i_low + 1;
                res[1] = i_high + 1;
                return res;
            } else if(sum < target) {
                //Sum too low. Increase i_low.
                i_low ++;
            } else {
                //Sum too high. Decrease i_high.
                i_high --;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        int[] res = twoSum(numbers, target);

        assert(res[0] == 1);
        assert(res[1] == 2);
    }
}
