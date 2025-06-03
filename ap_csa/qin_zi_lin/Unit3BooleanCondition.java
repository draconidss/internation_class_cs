public class Unit3BooleanCondition {

    // Unit3 Practice 40
    // public void someCode(int a, int b, int c) {
    //     if ((a < b) && (b < c)){
    //         return a;
    //     }
    //     if ((a >= b) && (b >= c)){
    //         return b;
    //     }
    //     if ((a == b) || (a == c) || (b == c)){
    //         return c;
    //     }
    //     return a;
    // }

    
    public static void main(String[] args) {
        // String compare via <
        String str1 = "abc", str2 = "def";
        if (str1 == str2){
            System.out.println(str1 + str2);
        }
        else{
            System.out.println(str2 + str1);
        }

        // If Condition
        boolean t = false;
        int a;
        int b;
        a = 2;
        b = 3;
        
        if (t || a <= b){
            System.out.println("It's");
            if (t) {
                int c = 0;
            }
            int d = 0;

        }
        else if (a > b){
            System.out.println("yes");
        }
        else {
            System.out.println("No");
        }

        // Unit3 Practice 46 - String object vs value
        String str1_1 = "ABC"; // different as String str1_1 = new String("ABC");
        String str2_1 = "ABC"; // different as String str1_2 = new String("ABC");
        System.out.println("str1_1 == str2_1:" + str1_1.equals(str2_1)); // compare their value
        System.out.println("str1_1 == str2_1:" + (str1_1 == str2_1)); // in this case, they are the same object


    }
}
