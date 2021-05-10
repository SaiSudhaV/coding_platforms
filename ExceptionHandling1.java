import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = 0;
        try{ 
            int i = sc.nextInt();
            int j = sc.nextInt();
            k = i / j;
            System.out.println(k);
        } catch(InputMismatchException e1){
            System.out.println("java.util.InputMismatchException");
        } catch (Exception e){
            System.out.println(e);
        }
    }
}

