import java.util.*;
class Addition{
    int add(int a, int b){
        int ans =a+b;
        return ans;
    }


}
public class sum_of_n_number {
    public static void main(String[] args) {
        Addition obj = new Addition();
        
       Scanner sc= new Scanner(System.in);   
       System.out.println("enter two number");
       int x =sc.nextInt();
       int y =sc.nextInt();
       int ans = obj.add(x , y);
       System.out.println("sum of two numbers is: " + ans);
    sc.close();
  }
    

 }
