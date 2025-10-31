

public class Unit1PrimitiveTypeOld {

    // primitive type
    public static void primitiveType() {
        // primitive type: int, double, boolean
        // initial syntax: primitiveType variableName = value;
        int int_1 = 1;
        // wrong: int int_2 = 1.0;
        System.out.println("int_1:" + int_1);

        double double_1 = 1.1;
        double double_2 = 1; // equal double double_2 = 1.0;
        System.out.println("double_1: " + int_1);
        System.out.println("double_2: " + int_1);

        boolean b_1 = true;
        boolean b_2 = false;
        System.out.println("b_1: " + b_1);
        System.out.println("b_2: " + b_2);

        // equal int int_3 = 1;
        int int_3;
        int_3 = 1;

        // string
        String str = "abc123__@";
        System.out.println("str: " + str);

        // cast 
        int DoubleToInt = (int) double_1;
        double IntToInt = (int) int_1;
        System.out.println("intToDouble: " + DoubleToInt);

        double IntToDouble = (double) int_1;
        double DoubleToDouble = (double) double_1;
        System.out.println("IntToDouble: " + IntToDouble);

        final int int_4 = 1;
        // wrong: int_4 = 2;
    }

    public static void math() {
        // int division and mod
        int int_1 = 5;
        int int_2 = 2;
        int int_3 = int_1 / int_2;
        int int_4 = int_1 % int_2;
        System.out.println("int_1 / int_2 = " + int_3); // 2
        System.out.println("int_1 % int_2 = " + int_4); // 1

        // three ways to increment
        int_1 = int_1 + 1;
        System.out.println("int_1 = int_1 + 1: " + int_1);
        int_1 += 1;
        int_1++;

        // do not compare double with ==
        double d1 = 1.1;
        double d2 = 0;

        // wrong d1 == d2;
        double d3 = d1 / d2;

    }


    

    public static void main(String[] args) {
        // primitiveType();
        math();
    }
}