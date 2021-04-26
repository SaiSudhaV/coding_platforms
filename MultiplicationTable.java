package c05022020;

import java.util.Scanner;

public class MultiplicationTable {

	public static void main(String[] args) {
		int n, k, count = 0;
		int[][] arr = new int[10000][10000];
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
	    for(int i = 0; i < n; i++){
	        for(int j = 0; j < n; j++){
	            arr[i][j] = (i + 1) * (j + 1);
	            if(arr[i][j] == k)
	                count++;
	        }
	    }
	    System.out.println(count);
	}

}
