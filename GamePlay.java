import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class GamePlay {

    public static void main(String[] args) throws java.lang.Exception{
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t > 0) {
            String s = sc.next();
            int temp[] = new int[26];
            for(int i = 0; i < s.length(); i++)
                temp[s.charAt(i) - 97]++;
            int res = 0;
            for(int i = 0; i < 26; i++)
                res ^= temp[i];
            if(res != 0)
                System.out.println("Santa");
            else
                System.out.println("Banta");
            t--;
        }
    }
}