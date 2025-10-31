

import java.util.Scanner;

public class Lecture2Lab1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int pen = scanner.nextInt();
        int pencil = scanner.nextInt();

        System.out.println("There are " + pen + " pens");
        System.out.println("There are " + pencil + " pencils");
        System.out.println("Total is " + (pen + pencil) + " pens and pencils");
    }
}
