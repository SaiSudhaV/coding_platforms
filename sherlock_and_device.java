import java.io.*;i
import java.util.*;
class MyScanner {
	BufferedReader br;
	StringTokenizer st;	
	public MyScanner() {
		br = new BufferedReader(new InputStreamReader(System.in));
	}
	String next() {
		while (st == null || !st.hasMoreElements()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				e.printStackTrace();
			}		}
		return st.nextToken();
	}
	
	int nextInt() {
		return Integer.parseInt(next());	
	}
	long nextLong() {
		return Long.parseLong(next());
	}
	
	double nextDouble() {
		return Double.parseDouble(next());						        
	}
	String nextLine(){
		String str = "";
		try {
			str = br.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return str;
	}
}
class hashmap {
	public static PrintWriter out;
	static Integer[] arr;
	static ArrayList<Integer>[] adj;
	static Boolean[] visited;
	static Integer[][] dp;
	public static void main(String args[]) throws Exception {
		
		MyScanner sc = new MyScanner();
		out = new PrintWriter(new BufferedOutputStream(System.out));
		
		int n = sc.nextInt();
		
		arr = new Integer[n+1];
		visited = new Boolean[n+1];
		adj = new ArrayList[n+1];
		dp = new Integer[1024][n+1];		
		for(int i = 0 ; i < 1024 ; i++){
			for(int j = 0 ; j < n+1 ; j++){
				dp[i][j]=-1;
			}
		}
		
		for (int i = 1 ; i < n+1 ; i++)
			adj[i] = new ArrayList<Integer>();
		
		for (int i = 1 ; i < n+1 ; i++)
			visited[i] = false;
		
		for (int i = 1 ; i < n+1 ; i++)
			arr[i] = sc.nextInt();
		
		for(int i = 1 ; i < n ; i++){
			int v = sc.nextInt(),u = sc.nextInt();
			adj[v].add(u);
			adj[u].add(v);
		}
		out.println(func(1, 0, 0));
		out.close();
		
	}
	
	static Integer func(int i, int count, int xor){
		visited[i] = true;
		if(adj[i].size() == 0){
			visited[i] = false;
			return arr[i];
		}
		
		if(count == 0 && adj[i].size() == 1 && visited[adj[i].get(0)]){
			visited[i] = false;
			return arr[i];
		}
		
		int sumWithout = 0;
		for(Integer j : adj[i]){
			if(!visited[j]){
				sumWithout += func(j, count>0 ? count - 1 : count, xor);
			}
		}		
		int sumWith = 0;
		int xor_copy = xor;
		if(count == 0){
			if(dp[xor][i] != -1){
				visited[i] = false;
				return dp[xor][i];
			}
			sumWith = arr[i];
			xor_copy = xor_copy^arr[i];
			count = xor_copy;
			for(Integer j : adj[i]){
				if(!visited[j]){
					sumWith += func(j, count, xor_copy);
				}
			}
			dp[xor][i] = Math.max(sumWith, sumWithout);
		}
		visited[i] = false;
		return Math.max(sumWith, sumWithout);
	}
}
