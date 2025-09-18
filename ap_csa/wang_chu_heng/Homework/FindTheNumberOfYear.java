package ap_csa.wang_chu_heng.Homework;

import java.util.Scanner;

public class FindTheNumberOfYear {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of minutes: ");
        int numberOfMinute = input.nextInt(); //Write your code here

        int years = numberOfMinute / (60 * 24 * 365);
        int days = (numberOfMinute % (60 * 24 * 365)) / 60 / 24;
        System.out.println(numberOfMinute + " minutes is approximately " + years + " and " + days + " days");
    }
}