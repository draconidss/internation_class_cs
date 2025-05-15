import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

// By Rico
public class RicoGradeAnalyzer {

    public static void main(String[] args) {
        Scanner mainScanner = new Scanner(System.in);
        ArrayList<Integer> grades = inputGrades(mainScanner);
        
        if (grades.isEmpty()) {
            System.out.println("No valid grades entered!");
            mainScanner.close();
            return;
        }

        double average = calculateAverage(grades);
        int max = findMax(grades);
        int min = findMin(grades);
        
        System.out.println("\n===== Grade Analysis Report =====");
        System.out.printf("Average: %.1f\n", average);
        System.out.println("Highest Grade: " + max);
        System.out.println("Lowest Grade: " + min);
        System.out.println("Overall Grade Level: " + getGradeLevel(average));

        mainScanner.close();
    }

    public static ArrayList<Integer> inputGrades(Scanner scanner) {
        ArrayList<Integer> grades = new ArrayList<>();
        System.out.println("Please enter student grades (enter -1 to finish):");

        //1. 该 procedure inputGrades 的 parameter 是 Scanner 类型，它是一个输入流对象。
        //2. 该 scanner 提供了一个方法 nextInt()，用于读取用户输入的学生成绩，并不会直接影响不同 code segments 的执行。
        //3. 但是 scanner 会根据监听不同的用户输入来执行不同的 code segments。
        //4. explain different code segments
        
        while (true) {
            System.out.print("Grade: ");
            int grade = scanner.nextInt();
            if (grade == -1)
                break;
            if (grade >= 0 && grade <= 100) {
                grades.add(grade);
            } else {
                System.out.println("Invalid grade (please enter an integer between 0 and 100)!");
            }
        }

        return grades;
    }

    public static double calculateAverage(ArrayList<Integer> grades) {
        int sum = 0;
        for (int grade : grades) {
            sum += grade;
        }
        return (double) sum / grades.size();
    }

    public static int findMax(ArrayList<Integer> grades) {
          int max = grades.get(0);
          for (int grade : grades) {
              if (grade > max) max = grade;
          }
          return max;
      }

    public static int findMin(ArrayList<Integer> grades) {
        int min = grades.get(0);
        for (int grade : grades) {
            if (grade < min) min = grade;
        }
        return min;
    }

    public static char getGradeLevel(double average) {
        if (average >= 90) return 'A';
        else if (average >= 80) return 'B';
        else if (average >= 70) return 'C';
        else if (average >= 60) return 'D';
        else return 'F';
    }
}