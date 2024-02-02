import java.util.Scanner;

public class switchprogram {
public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    System.out.println("enter any no. : ");
    int num=sc.nextInt();
    switch(num){
        case 1:
        System.out.println("mayank kumar");
        break;
        case 2:
        System.out.println("yashika haryana");
        break;
        case 3:
        System.out.println("aditya");
        break;
        case 4:
        System.out.println("Ashutrosh munger");
        break;
        case 5:
        System.out.println(" mukul mukama");
        break;
        case 6:
        System.out.println("bikki and vikas");
        break;
        case 7:
        System.out.println("lukki kumari");
        break;
        default:
        System.out.println("out of friend zone");
        sc.close();

    }
}
}
