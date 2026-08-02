import java.io.*;
import java.math.*;
import java.util.*;
import static java.lang.System.out;

public class majority_opinion {
	
	
	public static void main(String[] args) throws IOException {
		Scanner io = new Scanner(System.in);
		
		int t = io.nextInt();
		
		while (t > 0) {
			int n = io.nextInt();
			
			TreeSet<Integer> ans = new TreeSet<Integer>();
			
			int[] a = new int[n];
			
			for (int i = 0; i < n; i++) {
				a[i] = io.nextInt();
			}
			
			for (int i = 0; i < n; i++) {
				if (i - 1 >= 0 && a[i-1] == a[i])
					ans.add(a[i]);
				else if (i + 1 < n && a[i+1] == a[i])
					ans.add(a[i]);
				else if (i - 1 >= 0 && i + 1 < n && a[i-1] == a[i+1])
					ans.add(a[i-1]);
			}
			
			String s = "";
				
			for (int x : ans) {
				s += x + " ";
			}
			if (s.length() > 0) s = s.substring(0,s.length()-1);
			
			out.print(s);
			
			if (ans.isEmpty()) out.print(-1);
			
			
			if (t != 1) out.println();
			
			t--;
		}
		
		io.close();
		
	}
	
}

