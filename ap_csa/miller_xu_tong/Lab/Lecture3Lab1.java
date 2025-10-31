

import java.util.Scanner;

public class Lecture3Lab1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a1 = scanner.nextDouble();
        double a2 = scanner.nextDouble();
        double a3 = scanner.nextDouble();
        System.out.println("Enter grade: " +(int)a1);
        System.out.println("Enter grade: " + (int)a2);
        System.out.println("Enter grade: " + (int)a3);
        
        double average = (a1 + a2 + a3) / 3;
        System.out.println("Average = " + average);

        double b1 = Math.pow(a1 - average, 2);
        double b2 = Math.pow(a2 - average, 2);
        double b3 = Math.pow(a3 - average, 2);
        double Variance = (b1 + b2 + b3) / 3;
        System.out.println("Variance = " + Variance);

        double deviation = Math.sqrt(Variance);
        System.out.println("Standard deviation = " + deviation);
        
    }
}
