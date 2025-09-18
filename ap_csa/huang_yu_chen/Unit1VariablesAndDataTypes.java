package ap_csa.huang_yu_chen;

public class Unit1VariablesAndDataTypes {
    public static void main(String[] args) {
        //run-time error:Division by zero
        // System.out.println(10 / 0);

        // declare variable way1: decalre and initial
        int age = 18;

        // way2: decalre and initial
        int number;
        number = 10;

        int width = 10;
        int perimeter = 4 * width;

        int abc = 5;
        System.out.println(abc);

        int int_1 = 10;

        // use % 2 to judge odd or even
        System.out.println("1 % 2: " + (1 % 2)); // 1: odd
        System.out.println("0 % 2: " + (0 % 2)); // 0: even
        System.out.println("79 % 2: " + (79 % 2)); // 1: odd
        System.out.println("764 % 2: " + (764 % 2)); // 0: odd

        // final
        final double PI;
        PI = 9.9;
        final double TAX_RATE = 6.67;
        // PI = 111;// Error: The final variable PI cannot be changed

        int x = 3;
        int y = 4;
        x*=y+2;
        x++;
        System.out.println("x: " + x);

        // int MAX_VALUE and MIN_VALUE
        // int n = 100000000000000; //Error:n is out of range
        int intMaxValue = Integer.MAX_VALUE;
        System.out.println("intMaxValue: " + intMaxValue);
        int intMinValue = Integer.MIN_VALUE;
        System.out.println("intMinValue: " + intMinValue);

        int m;
        double n = 66.69;
        m =(int)n;//m is 66
    }
}
