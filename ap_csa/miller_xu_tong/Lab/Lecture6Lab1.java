import java.util.Scanner;

public class Lecture6Lab1 {

    public static void extractName() {
        Scanner scanner = new Scanner(System.in);
        String a = scanner.nextLine();
        int index = a.indexOf(" ");
        String firstName = a.substring(0, index - 1);
        String temp = a.substring(index + 1);
        int index1 = temp.indexOf(" ");
        String middleName = temp.substring(0, index1 - 1);
        String lastName = temp.substring(index1 + 1);
        System.out.println("first: " + firstName);
        System.out.println("middle: " + middleName);
        System.out.println("last: " + lastName);

    }

    public static String pigLatin() {
        Scanner scanner = new Scanner(System.in);
        String b = scanner.nextLine();
        String letter = b.substring(0, 1);
        String letter2 = b.substring(1);
        return letter2 + letter + "ay";
    }

    public static void main(String[] args) {
        // extractName();
        String c = pigLatin();
        System.out.println(c);
    }
}
