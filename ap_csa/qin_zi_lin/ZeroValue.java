public class ZeroValue {
    final static int classVariable = 1;

    boolean classVariable_2;

    public static void main(String[] args) {
        // local variable
        int localV = 1;
        System.out.println(localV);

        // class attribute
        ZeroValue zv = new ZeroValue();
        System.out.println(classVariable);
        System.out.println(zv.classVariable_2);
    }
}
