import java.io.*;
import java.util.*;
public class  Main{ 
	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] n = br.readLine().split("");
		String[] arr = new String[n.length];
		Arrays.sort(n);
		for(int i=0;i<n.length;i++) {
			arr[i] = n[n.length-i-1];
		}
		for(String item : arr)
			System.out.print(item);
	}     
} 

