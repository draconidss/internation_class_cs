package ap_csa.wang_chu_heng.Homework;

import java.util.Scanner;

public class ConvertPoundToKg {
    public static void main(String[] args) {
        System.out.println("Enter a number in pounds: ");
        Scanner input = new Scanner(System.in);
        double pound = input.nextDouble();
        
        //Write your code here
        double kg = pound * 0.454; // calculate the kilograms from pounds
        System.out.println(pound + " pounds is " + kg + " kilograms"); // print the pound and kilograms
    }
}