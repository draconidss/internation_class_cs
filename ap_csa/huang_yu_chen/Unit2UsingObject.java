// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).
package ap_csa.huang_yu_chen;

public class Unit2UsingObject {
   public Unit2UsingObject() {
   }

   public static void main(String[] var0) {
      System.out.println("a");
      System.out.println();
      System.out.println("b");

      String str = "hello";
      int strLength = str.length();
      System.out.println(strLength);
      // System.out.println("aab\nbcc\"\\");

      // subString
      String greeting = "Hello, World!";
      String sub = greeting.substring(0,5);//sub is "Hello"
      String sub2 = greeting.substring(7, 12);//sub2 is "World"
      System.out.println("sub: " + sub);
      System.out.println("sub2: " + sub2);
      System.out.println("greeting: " + greeting);

      // string compareTo()
      String eSent = "hello333";
      String fSent = "hello299";
      String gSent = "abc";
      System.out.println(eSent.compareTo(fSent));//value<0
      System.out.println(eSent.compareTo(gSent));//value >0
   }
}
