package ap_csa.miller_xu_tong;

public class Unit2UsingObject {
    public static void main(String[] args) {
        System.out.println("abc\ndef");
        System.out.println("a\\bc\n \" \ndef");

        // Length()
        String aSent = "winter is coming!";
        int senLength = aSent.length();
        System.out.println(senLength);
        System.out.println("abc".length());
    }
}
