public class Unit5WritingClasses {
    public static class Student {
        private String name;
        private int grade;

        public Student() {
            System.out.println("No name, No grade");
        }

        public Student(String studentName, int studentGrade){
            name = studentName;
            grade = studentGrade;
        }

        public void printGrade(){
            System.out.println(grade);
        }

        private void printName(){ // private: only used in the same file
            System.out.println(name);
        }
        
    }

    public static void StudentWithArgConstructor() {
        Student a = new Student();
        Student b = new Student("draco", 100);
        Student c = new Student("alex", 88);
        b.printGrade();
        b.printName();
    }


    // remember: always set the instance attributes PRIVATE
    private int intAttr;
    private Double doubleAttr = new Double(0.0);
    private boolean boolAttr;   
    private String stringAttr = new String();

    public int publicIntAttr;

    public static void printDefaultAttrValue() {
        Unit5WritingClasses obj1 = new Unit5WritingClasses();
        System.out.println(obj1.intAttr);
        System.out.println(obj1.doubleAttr);
        System.out.println(obj1.boolAttr);
        System.out.println(obj1.stringAttr);
    }
    
    public static void main(String[] args) {
        printDefaultAttrValue();
        StudentWithArgConstructor();
    }
}