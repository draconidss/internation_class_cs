package ap_csa.xu_chen_rui;

public class Unit2UsingObjects {
    
    public static void Strings() {
        // two ways declare String
        String str1 = "abc__1";
        String str2 = new String("abc__1");
        System.out.println("str1:" + str1);
        System.out.println("str2:" + str2);

        // empty String, not null
        String str3 = new String("");

        // declare String, is null
        String str4;

        // String concatenation
        String str5 = str1 + str2;
        System.out.println("str5:" + str5);

        // String concatenation: int and String
        int int1 = 5;
        String str6 = "10";
        String str7 = str6 + int1;
        System.out.println("str7:" + str7); // str7:105

        // String concatenation: two int and String
        int int2 = 1;
        int int3 = 2;
        String str8 = "10";
        String str9 = str8 + int2 + int3;
        String str10 = int2 + int3 + str8;
        String str11 = int2 + str8 + int3;
        String str12 = str8 + (int2 + int3);
        System.out.println("str9:" + str9); // "1012"
        System.out.println("str10:" + str10); // "310"
        System.out.println("str11:" + str11); // "1102"
        System.out.println("str12:" + str12); // "103"

        // compare String with ==
        boolean com1 = (str1 == str2);
        System.out.println("com1:" + com1); // false

        // compre String with equals(), it's case-sensitive
        String username1 = "Cat Lady";
        String username2 = "Cat lady";
        System.out.println(username1.equals("Cat Lady")); // true
        System.out.println(username2.equals("Cat Lady")); // false

        System.out.println(username1.equals(username2)); // false

        // compare String with compareTo()
        // result is 0
        String str13 = "Hello";
        String str14 = "Hello";
        int str13CompareStr14 = str13.compareTo(str14);
        System.out.println("str13.compareTo(str14):" + str13CompareStr14); // 0

        // result i negative, J is above 2 from H in ASCII
        String str15 = "Hello";
        String str16 = "JflloaA";
        int str15CompareTostr16 = str15.compareTo(str16);
        int str16CompareTostr15 = str16.compareTo(str15);
        System.out.println("str15.compareTo(str16):" + str15CompareTostr16); // -2
        System.out.println("str16.compareTo(str15):" + str16CompareTostr15); // 2
        

    }

    public static void main(String[] args) {
        Strings();
    }
}
