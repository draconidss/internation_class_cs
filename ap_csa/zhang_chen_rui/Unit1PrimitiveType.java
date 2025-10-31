

public class Unit1PrimitiveType {

    public static void WrongVariables() {
        // System.out.println(number); // undeclared

        int width;
        // System.out.println(width); // uninitialed

        int height;
        // int height = 10; // duplicate

        int my_computer, getName, name4;
        // int get?Name, 4name, int; // wrong name
    }

    public static void dataTypes() {
        int number = 10;
        double price_1 = 28.99;
        double price_2 = 20;
        boolean flag = true;
        String str = "Hello";

        System.out.println("number: " + number);
        System.out.println("price_1: " + price_1);
        System.out.println("price_2: " + price_2);
        System.out.println("flag: " + flag);
        System.out.println("str: " + str);
    }

    public static void arithmetic() {
        System.out.println("10.0 / 4.0: " + 10.0 / 4.0); // 2.5
        System.out.println("10 / 4.0: " + 10 / 4.0); // 2.5
        System.out.println("10.0 / 4: " + 10.0 / 4); // 2.5
        System.out.println("10 / 4: " + 10 / 4); // 2
        // System.out.println("10 / 0: " + 10 / 0); // error
        System.out.println("10 / 3 + 10 % 3:" + (10 / 3 + 10 % 3));
    }

    public static void castingAndRangeOfVariable() {
        // int n = 100000000000;
        System.out.println(Integer.MAX_VALUE); // 2147483647
        System.out.println(Integer.MIN_VALUE); // -2147483648
        int m = 25;
        double n = 66.69;
        n = m; // safe
        // m = n; // unsafe
        m = (int)66.69;// safe: m is 66
        System.out.println("n:" + n);
        System.out.println("m:" + m);

        int total = 10;
        int count = 3;
        double result = (double) total / count;// result is 3.33
        System.out.println("result:" + result);

    }

    public static void main(String[] args) {
        System.out.print("Hello ChenRui!");
        // System.out.println("Hello World!");
        System.out.println("Hello World");
        System.out.println("Hello World");

        dataTypes();
        arithmetic();
        castingAndRangeOfVariable();
    }
}
