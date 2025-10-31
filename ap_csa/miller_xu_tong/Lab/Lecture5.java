import java.util.Scanner;

public class Lecture5 {
    public static double average(int x, int y) {
        double average = (x + y) / 2.0;
        return average;
    }

    public static double slope(int x1, int y1, int x2, int y2) {
        double slope = (double) (y2 - y1) / (x2 - x1);
        return slope;

    }

    public static void main(String[] args) {
        double average = average(10, 25);
        System.out.println(average);
    }
}
