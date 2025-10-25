package ap_csa.miller_xu_tong.Lab;

import java.util.Scanner;

public class Lecture9Lab1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double height = scanner.nextDouble();
        double weight = scanner.nextDouble();
        double bmi = (weight / Math.pow(height, 2)) * 703;
        System.out.println("Height (in inches): " + height);
        System.out.println("Weight (in pounds): " + weight);
        System.out.println("BMI = " + bmi);

        if (bmi < 18.5) {
            System.out.println("underweight");
        } else if (bmi < 25) {
            System.out.println("normal");
        } else if (bmi < 30) {
            System.out.println("Overweight");
        } else {
            System.out.println("obese");
        }
    }
}
