package ap_csa.zhang_chen_rui;

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

    public static void main(String[] args) {
        System.out.print("Hello ChenRui!");
        // System.out.println("Hello World!");
        System.out.println("Hello World");
        System.out.println("Hello World");

        dataTypes();
        arithmetic();
    }
}
