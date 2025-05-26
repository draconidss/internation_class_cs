public class Unit2UsingObject {
    // try out
    public static void example(Integer a, Double b, Boolean t) {
        System.out.println("a:" + a);
        System.out.println("b:" + b);
        System.out.println("t:" + t);
    }
    
    
    public static void main(String[] args) {
        System.out.println("====================================Packaging Class====================================");

        // Packaging Primitive Type from int to Integer
        int a;
        a = new Integer(10);
        Integer b = new Integer(10);
        System.out.println("a:" + a);
        System.out.println("b:" + b);
        System.out.println("b.intValue():" + b.intValue());
        // a is still a primitive type that int, can't invoke method
        // System.out.println("a.intValue():" + a.intValue());

        // Packaging Primitive Type from boolean to Boolean
        boolean t;
        t = new Boolean(true);
        Boolean t1 = new Boolean(true);
        System.out.println("t:" + t);
        // t1.booleanValue() return boolean from Boolean
        System.out.println("t1.booleanValue():" + t1.booleanValue());
        // t is still a primitive type boolean, can't invoke method
        // System.out.println(t.booleanValue());

        // Packaging Primitive Type from double to Double
        double c;
        c = new Double(9.9);
        // System.out.println(c.doubleValue()); // Cannot invoke doubleValue() on the primitive type double
        Double d = new Double(10.0);
        System.out.println(d.doubleValue());

        // test
        int num = 1;
        double num2 = 2.0;
        boolean t3 = true;
        example(num, num2, t3);

    }
    
}
