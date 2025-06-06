public class Unit4Iteration {

    // infiniteLoop
    public void infiniteLoop() {
        // infinite for interation
        for (int i = 10; i >= 10; i++){
            System.out.println(i);
        }
    
        // infinite while iteration
        int i = 10;
        while (i >= 10){
            System.out.println(i);
            i++;
        }
    }
    
    // Find all the factors of an integer (n)
    public static void factors(int n){
        System.out.println("factors of :" + n);
        int i = 1;
        while (i <= n){
            if (n % i == 0){
                System.out.println("the factor of " + n + " is:" + i);
            }
            i++;
        }
    }
    
    // Find the sum of all the digits in an integer (n)
    public static void sumOfDigits(int n){
        System.out.print("sum of digits of " + n + " is: ");
        int sum = 0;
        while (n >= 0){
            if (n > 10){
                sum += (n % 10); // last digit
                n /= 10; // remove the last digit     
            }
            else { // when n <= 10
                sum += n;
                break; // terminate
            }
        }
        System.out.println(sum);
    }
    // Reverse the order of the characters in a string.
    public static void reverseString(String str){
        String newString;
         
        // newString = chr + newString
        
    }
    // iteration: for 
    public static void forIteration() {
        // for iteration that print 0 to 4, code execute sequence:
        // step1: int i = 0;
        // step2: i < 5;
        // step3: System.out.println(i);
        // step4: i++;
        // step5: -> step2
        for (int i = 0; i < 5; i++) {
            System.out.println(i); // 0 1 2 3 4
        }
        
        // print 5 4 3 2 1
        for (int i = 5; i > 0; i--) {
            System.out.println("i:" + i); // 5 4 3 2 1
        }

        // declare control variable i in outside of for iteration
        int i;
        for (i = 0; i < 5; i++) {
            System.out.println(i);
        }
        System.out.println(i);

        // omit control variable and declare it in outside from for iteration
        // same as: for (int j = 0; j < 5; j++) {}
        int j = 0;
        for (; j < 5; j++) {}
        
        // omit control condition and declare it in body of iteration
        // same as: for (int k = 0; k < 5; k++) {}
        for (int k = 0;; k++) {
            if (k >= 5) {
                break; // exit iteration
            }
        }
        
        // omit variable modification and declare it in body of iteration
        // same as: for (int k = 0; k < 5; k++) {}
        for (int k = 0; k < 5;) {
            k++;
        }

        // omit control variable, condition and variable modification
        // same as: for (int k = 0; k < 5; k++) {}
        int k = 0;
        for (; ;) {
            if (k >= 5){
                break;
            }
            k++;
        }

        // custom for iteration sequence
        // k++; is execute before condition if (k >= 5);
        int y = 0;
        for (;;) {
            k++;
            if (k >= 5){
                break;
            }
        }
        
        // Find all the factors of an integer (n)
        factors(12);

        // Find the sum of digits of an integer (n)
        sumOfDigits(2345678);
    }

    public static void main(String[] args) {
        forIteration();
    }
}
