import java.util.*;
public class read_string {
    public static void main(String[] args) {
        //program to read a character from string
        System.out.println("enter string or character");
        Scanner sc = new Scanner(System.in);
        char ch= sc.next().charAt(0);
        
        System.out.println("chracter is : " + ch);
        sc.close();
    }
}
