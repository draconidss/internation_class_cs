package ap_csa.huang_yu_chen;

public class Unit3BooleanExpression {
    public static void main(String[] args) {
        System.out.println(4 > 1 * 3);
        System.out.println(4 < (1 * 3));

        double num = 15;
        boolean res3 = (num % 2 == 0);
        System.out.println("res3 is:" + res3);
    }
}