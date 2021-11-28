import java.math.BigInteger;
import java.util.List;

public class main {

    static class ListNode {
        public int val;
        ListNode next;

        ListNode() {

        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode();

        BigInteger sum1 = new BigInteger("0");
        BigInteger sum2 = new BigInteger("0");
        BigInteger multiplier = new BigInteger("1");

        // don't change reference of parameters
        ListNode _l1 = l1;
        ListNode _l2 = l2;

        while(_l1 != null) {
            sum1 = sum1.add(multiplier.multiply(BigInteger.valueOf(_l1.val)));
            _l1 = _l1.next;
            multiplier = multiplier.multiply(BigInteger.valueOf(10));
        }

        multiplier = BigInteger.valueOf(1);
        while(_l2 != null) {
            sum2 = sum2.add(multiplier.multiply(BigInteger.valueOf(_l2.val)));
            _l2 = _l2.next;
            multiplier = multiplier.multiply(BigInteger.valueOf(10));
        }

        System.out.println(sum1);
        System.out.println(sum2);

        BigInteger res_sum = sum1.add(sum2);
        ListNode res_pointer = res;


        while(res_sum.compareTo(BigInteger.valueOf(9)) > 0) {
            res_pointer.val = res_sum.mod(BigInteger.valueOf(10)).intValue();
            res_pointer.next = new ListNode();
            res_pointer = res_pointer.next;


            res_sum = res_sum.divide(BigInteger.valueOf(10));
        }

        res_pointer.val = res_sum.mod(BigInteger.valueOf(10)).intValue();

        return res;
    }

    public static void main(String[] args) {
//        {
//            ListNode l1 = new ListNode(2);
//            l1.next = new ListNode(4);
//            l1.next.next = new ListNode(3);
//
//            ListNode l2 = new ListNode(5);
//            l2.next = new ListNode(6);
//            l2.next.next = new ListNode(4);
//
//            ListNode res = addTwoNumbers(l1, l2);
//
//            assert (res.val == 7);
//            assert (res.next.val == 0);
//            assert (res.next.next.val == 8);
//        }

        {
            ListNode l1 = new ListNode(9);

            ListNode l2 = new ListNode(
                    1, new ListNode(
                            9, new ListNode(
                                    9, new ListNode(
                                            9, new ListNode(
                                                    9, new ListNode(
                                                            9, new ListNode(
                                                                    9, new ListNode(
                                                                            9, new ListNode(
                                                                                    9, new ListNode(
                                                                                            9))))))))));

            ListNode res = addTwoNumbers(l1, l2);
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 0);
            res = res.next;
            assert(res.val == 1);

            assert(res.next == null);
        }
    }
}
