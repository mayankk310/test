import java.util.Scanner;

public class test2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.print("Enter Your Age: ");
        // int x = sc.nextInt();
        // if(x >= 18)
        //     System.out.println("You Can Drive");
        // else
        //     System.out.println("You Can't Drive"); 


        // System.out.print("Enter your Age: ");
        // int age = sc.nextInt();
        // if(age < 18)
        //     System.out.println("Nabaalik");
        // else if(age >= 18 && age <= 24)
        //     System.out.println("Baalik");
        // else if(age >=24 && age <=30)
         //     System.out.println("Jawaan");
        // else
        //     System.out.println("Buddha");



            System.out.print("Enter Month: ");
            int month = sc.nextInt();
            switch (month) {
                case 1:
                case 3:
                case 5:
                case 7:
                case 8:
                case 10:
                case 12:
                    System.out.println("31 Days");
                    break;
                case 4:
                case 6:
                case 9:
                case 11:
                    System.out.println("30 Days");    
                    break;
                case 2:
                    System.out.println("28 Days");
                    break;        
                default:
                    System.out.println("Try again");
                    break;
            }

         


        sc.close();
    }
}
