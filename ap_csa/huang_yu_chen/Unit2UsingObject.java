// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).


public class Unit2UsingObject {
   public Unit2UsingObject() {
   }

   public static void main(String[] var) {
      System.out.println("a");
      System.out.println();
      System.out.println("b");

      String str = "hello";
      int strLength = str.length();
      System.out.println(strLength);
      // System.out.println("aab\nbcc\"\\");

      // subString
      String greeting = "Hello, World!";
      String sub = greeting.substring(0, 5);// sub is "Hello"
      String sub2 = greeting.substring(7, 12);// sub2 is "World"
      System.out.println("sub: " + sub);
      System.out.println("sub2: " + sub2);
      System.out.println("greeting: " + greeting);

      // string compareTo()
      String eSent = "hello333";
      String fSent = "hello299";
      String gSent = "abc";
      System.out.println(eSent.compareTo(fSent));// value<0
      System.out.println(eSent.compareTo(gSent));// value >0

      // wrapper class
      Integer integer_1 = new Integer(45);
      integer_1 = 100;
      int integer_int = integer_1.intValue(); // unboxing
      System.out.println("integer_1: " + integer_1);
      System.out.println("Integer.MIN_VALUE: " + Integer.MIN_VALUE);
      System.out.println("Integer.MAX_VALUE: " + Integer.MAX_VALUE);

      Integer obj3;
      int num3 = 69;
      obj3 = num3; // autoboxing
      obj3 = new Integer(num3); // boxing

      num3 = obj3; // unboxing
      num3 = obj3.intValue(); // unboxing

      System.out.println(0 < 20 && 20 < 18);

   }

   public static double name() {
      return 100; // auto cast to 100.0

   }
}
