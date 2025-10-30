package java_study.lang_jun_yu.homework;

public class Hotel {

    // MAIN METHOD: Entry point of the Java program
    public static void main(String args[]) {

        // INPUT SECTION: Identifies and initializes input variables
        double priceInput = 40; // Mock Input: Cost per night value in euros
        double distanceInput = 2; // Mock Input: Distance value in kilometers

        if (priceInput < 0 || distanceInput < 0) {
            System.out.println("Inputs cannot be nagative!");
        } else if (priceInput > 40 || distanceInput > 3) {
            System.out.println("Dont Book!Too expensive. Price should not exceed €40/night");
            System.out.println("Too far. Distance should not exceed 3 km");
        } else if (priceInput > 40) {
            System.out.println("Dont Book!Too expensive. Price should not exceed €40/night");
        } else if (distanceInput > 3) {
            System.out.println("Dont Book!Too far. Distance should not exceed 3 km");
        } else {
            System.out.println("Book!");
        }
    }
}