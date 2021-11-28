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

        long sum1 = 0;
        long sum2 = 0;
        long multiplier = 1;

        // don't change reference of parameters
        ListNode _l1 = l1;
        ListNode _l2 = l2;

        while(_l1 != null) {
            sum1 += (multiplier * (_l1.val));
            _l1 = _l1.next;
            multiplier *= 10;
        }

        multiplier = 1;
        while(_l2 != null) {
            sum2 += (multiplier * (_l2.val));
            _l2 = _l2.next;
            multiplier *= 10;
        }

        System.out.println(sum1);
        System.out.println(sum2);

        long res_sum = sum1 + sum2;
        ListNode res_pointer = res;

        while(res_sum > 9) {
            res_pointer.val = (int)(res_sum % 10);
            res_pointer.next = new ListNode();
            res_pointer = res_pointer.next;

            res_sum /= 10;
        }

        res_pointer.val = (int)(res_sum % 10);

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
