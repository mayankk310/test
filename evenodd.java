import java.util.*;
public class evenodd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number");
        Float num = sc.nextFloat();
        // if(num%2==0){
        //     System.out.println("even");
        // }else{
        //     System.out.println("odd");
        // }
        String a;
        a=(num  %2 ==0) ?  "even" : "odd";
        System.out.println(a);
        sc.close();
    }
    
}
