import java.util.Scanner;


public class swaping_of_two_no {
    public static void main(String[] args) {
        int arr[];
        arr= new int[10];
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size of array");
        int n = sc.nextInt();
        System.out.println("Enter elements");
        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt(); 
        }
        System.out.println("Before change");
        for(int i = 0; i < n; i++)
        {
            System.out.println(arr[i]); 
        } 
        System.out.println("enter position to swap");
        int temp;
        int x = sc.nextInt();
        int y = sc.nextInt();
        temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
        System.out.println("After change");
        for(int i = 0; i < n; i++)
        {
            System.out.println(arr[i]); 
        } 
        sc.close();
    }
}
