

import java.util.Scanner;

public class MaximumNum {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt();
        int num2 = input.nextInt();
        int num3 = input.nextInt();

        if (num1 > num2) {
            if (num1 > num3) {
                System.out.println(num1 + " is the maximum");
            } else {
                System.out.println(num3 + " is the maximum");
            }
        } else {
            if (num2 > num3) {
                System.out.println(num2 + " is the maximum");
            } else {
                System.out.println(num3 + " is the maximum");
            }
        }
    }
}