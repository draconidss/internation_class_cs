public class Unit4Practice {

    // CSA Practice 19
    public static void no19() {
        int n1 = 0;
        int n2 = 3;
        while ((n2 != 0) && ((n1 / n2 >= 0))){ // ArithmeticException: / by zero
            // but when n2 = 0, doesn't the evaluation stops at (n2 != 0) bc this already evaluates to false??
            n1 = n1 + 2;
            n2 = n2 - 1;
            System.err.println("n1:" + n1);
            System.err.println("n1:" + n1);
        }
        System.out.println("n1: " + n1);
        System.out.println("n2: " + n2);
    }

    // 22
    public static String abMethod(String a, String b){
        int x = a.indexOf(b);
        while (x >= 0){
            System.out.println("a:" + a);
            System.out.println("x:" + x);
            int newLength = x + b.length();
            System.out.println("newLength:" + newLength);
            System.out.println("a.substring(newLength)" + a.substring(newLength));
            a = a.substring(0, x) + a.substring(newLength);
            // why doesn't this give a StringIndexOutOfBoundException error?
            x = a.indexOf(b);
        }
        return a;
    }

    public static void main(String[] args) {
        // no19();
        // abMethod("sing the song", "ng");
        String str = "sing the son";
        System.out.println("str.length():" + str.length());
        System.out.println(str.substring(str.length()));
    }
}