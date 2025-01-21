"""write a program that accept two integer values and if both are equal
then prints same identity otherwise prints Different identity"""

import java.util.Scanner;

public class IdentityCheck {
    public static void main(String[] args) {
       
        Scanner scanner = new Scanner(System.in);
        
       
        System.out.print("Enter the first integer: ");
        int num1 = scanner.nextInt();
        
        System.out.print("Enter the second integer: ");
        int num2 = scanner.nextInt();
        
        
        if (num1 == num2) {
            System.out.println("Same identity");
        } else {
            System.out.println("Different identity");
        }
        
      
        scanner.close();
    }
}


