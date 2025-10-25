package java_study.lang_jun_yu.homework;

public class MyClassCorrect {

    // MAIN METHOD: Entry point of the Java program
    public static void main(String args[]) {

        // INPUT SECTION: Identifies and initializes input variables
        double costPerNight = 40; //Mock Input: Cost per night value in euros
        double distance = 2; //Mock Input: Distance value in kilometers

        // Check if both cost and distance are within valid booking limits
        if ((costPerNight >= 0 && costPerNight <= 40) && (distance >= 0 && distance <= 3)) {
            // OUTPUT: booking success decision
            System.out.print("Book! cost is " + costPerNight + ", distance is " + distance + "km.");
        } else {
            // Handle cases where cost or distance are invalid
            // OUTPUT: Don't Book! decision with specific invalid reasons
            System.out.print("Don't Book! ");
            // Check and output invalid cost, cost is less than 0 or greater than 40
            if (costPerNight < 0 || costPerNight > 40)
                // OUTPUT: Invalid cost value and error message
                System.out.println("Invalid cost! cost is " + costPerNight + ", should be between €0.00 and €40.00!");
            // Check and output invalid distance, distance is less than 0 or greater than 3
            if (distance < 0 || distance > 3)
                // OUTPUT: Invalid distance value and error message
                System.out.println("Invalid distance! distance is " + distance + "km, should be between 0km and 3km!");
        }
    }
}