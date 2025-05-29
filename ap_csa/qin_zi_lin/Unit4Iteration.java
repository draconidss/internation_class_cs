public class Unit4Iteration {

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

    }

    public static void main(String[] args) {
        forIteration();
    }
}
