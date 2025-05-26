public class Unit1PrimitiveType {
    public static void main(String[] args) {
        double roundMe = 53.6;
        int result = (int)(roundMe + 0.5);
        System.out.println(result);


        double roundMe1 = -53.6;
        int result1 = (int)(roundMe1 - 0.5);
        System.out.println(result1);

        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);

        // compare round off
        double num1 = 3.99999;
        double num2 = 4.0;
        System.out.println(num1==num2);
        double tolerance = 0.0001;
        boolean result3 = Math.abs(num1-num2) <= tolerance;
        System.out.println(result3);

        // int 和 double 之间的转换
        double sum = 1.0;
        int avg = 1;
        // int num3 = sum / avg;
        
        // String
        String str = "123Hello";
        System.out.println(str);

        String str1 = new String("3456789hello");
        System.out.println(str1);

        // String empty; 
        String empty = new String();

        System.out.println(empty);

        // *
        // String str3 = "cat";
        // System.out.println(str3 * 10);

        String firstName = "John";
        int swag = 10, swag1 = 20;
        boolean isTrue = true;
        System.out.println(swag + firstName + isTrue);
    }
}