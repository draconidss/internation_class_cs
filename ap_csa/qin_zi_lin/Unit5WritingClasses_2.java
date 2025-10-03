
public class Unit5WritingClasses_2 {
     public static void testPrivateAndPublic() {
        Unit5WritingClasses obj = new Unit5WritingClasses();
        System.out.println(obj.publicIntAttr);
        Unit5WritingClasses.Student stu = new Unit5WritingClasses.Student();

        stu.printGrade();
        // stu.printName();

    }

    public static void main(String[] args) {
        testPrivateAndPublic();
    }
}
