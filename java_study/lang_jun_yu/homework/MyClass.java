package java_study.lang_jun_yu.homework;

public class MyClass {

    // MAIN METHOD: Entry point of the Java program
    public static void main(String args[]) {

        // INPUT SECTION: Identifies and initializes input variables
        double cost = 40.21; // Input: Cost value in euros
        double distance = 4.5; // Input: Distance value in kilometers

        if (cost >= 0 && distance >= 0) {

            // Uses logical OR (||) to check multiple conditions

            // This condition seems logically flawed - it should likely use AND instead of
            // OR
            if (cost > 40 || distance <= 3)
                // OUTPUT: Warning about cost constraint
                System.out.println("Don't Book! Cost should be no more than €40.00!");

            // This condition also appears logically problematic
            else if (cost <= 40 || distance > 3)
                // OUTPUT: Warning about distance constraint
                System.out.println("Don't Book! Distance should be no more than 3km!");

            // Uses logical OR which doesn't make sense for this condition
            else if (cost <= 40 || distance <= 3)
                // OUTPUT: Warning about both constraints
                System.out.println(
                        "Don't Book! Cost should be no more than €40.00 and distance should be no more than 3km!");

            // DEFAULT CASE: If none of the above conditions are met
            else
                // OUTPUT: Positive booking decision
                System.out.println("Book!");
        } else {

            // Handle cases where inputs are invalid (negative values)

            if (cost < 0)
                // OUTPUT: Invalid cost error message
                System.out.println("Invalid cost!");

            // NOTE: There's a typo in the variable name - should be "distance" not
            // "diatance"
            if (distance < 0) // This will cause a compilation error
                // OUTPUT: Invalid distance error message
                System.out.println("Invalid distance!");
        }
    }
}