import java.util.*;
public class sumOfnNaturalNumber {
 public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    System.out.println("enter total number to print: ");
    int n=24;
    int num=1,sum=0;
     while(num<n){
         System.out.println(num);
         sum=sum+num;
         num++;
         sc.close();
     }
     System.out.println("sum is : "+sum);
    for(num=1;num<n;num++){              //using for loop
        System.out.println(num);
        sum=sum+num;
    }
    System.out.println("sum is : "+sum);
}   
}
