import java.util.*;

public class ifelseif {
    public static void main(String[] args) {
        
  
    Scanner sc= new Scanner(System.in);
    System.out.println("enter age: ");
    Float age= sc.nextFloat();
 if(age<=12){
     System.out.println("children");
 }else if(age>12 && age<18){
        System.out.println("teenager");

    }else{
    //     System.out.println("adult");
    }
        sc.close();
    
 
}

}