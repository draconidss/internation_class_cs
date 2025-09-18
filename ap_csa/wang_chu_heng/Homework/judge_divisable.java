package ap_csa.wang_chu_heng.Homework;

import java.util.Scanner;

public class judge_divisable {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        
        if ((num % 5 == 0) && (num % 6 == 0)) {
            System.out.println(num + " can be divisable by 5 and 6");
        } 
        else if ((num % 5 == 0) && (num % 6 != 0)){
            System.out.println(num + " cannot be divisible by 5 and6 at the same time");
        }
        else if ((num % 5 != 0) && (num % 6 == 0)){

        }
    }
}
