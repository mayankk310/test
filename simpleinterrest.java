import java.util.*;
public class simpleinterrest {
   public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    System.out.println("enter principal rate and time : ");
    float p=sc.nextFloat();
    float r=sc.nextFloat();
    float t=sc.nextFloat();
    float si= (p*r*t)/100;
    float Total = si+p;
      System.out.println("principal : "+p);
System.out.println("rate :"+r);
System.out.println("time: "+t);
System.out.println("si="+si);
System.out.println("Total amount= "+Total);
sc.close();
   } 
}
