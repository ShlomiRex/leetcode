public class main {
    private static int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++) {
            int find = (target - nums[i]);
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[j] == find) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        int[] res = twoSum(numbers, target);
        assert(res[0] == 0);
        assert(res[1] == 1);
    }


}
