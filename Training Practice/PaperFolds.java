/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;

public class PaperFolds {
    private int h;
    private int h1;
    private int w;
    private int w1;
    private int res;
    
    public int min_moves(int h, int h1, int w, int w1) {
        res = 0;
        while(h > h1){
            if((h / 2) < (h - h1))
                h = h / 2;
            else 
                h = h1;
            ++res;
        }
        while(w > w1){
            if((w / 2) < (w - w1))
                w = w / 2;
            else 
                w = w1;
            ++res;
        }
        return res;
    }

    public static void main(String[] args) {
        PaperFolds obj = new PaperFolds();
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int h1 = sc.nextInt();
        int w = sc.nextInt();
        int w1 = sc.nextInt();
        System.out.println((h < h1) || (w < w1));
        if(!((h < h1) || (w < w1)))
            System.out.println(obj.min_moves(h, h1, w, w1));
    }
}