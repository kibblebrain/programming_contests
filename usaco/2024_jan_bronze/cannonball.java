import java.io.*;
import java.math.*;
import java.util.*;
import static java.lang.System.out;

public class cannonball {
	
	
	public static void main(String[] args) throws IOException {
		Scanner io = new Scanner(System.in);
		
		int n = io.nextInt();
		int s = io.nextInt()-1;
		
		int[][] a = new int[n][2];
		
		
		for (int i = 0; i < n; i++) {
			a[i][0] = io.nextInt();
			
			a[i][1] = io.nextInt();
			
		}
		
		int power = 1;
		int dir = 1;
		
		int incr = 1;
		
		int ans = 0;
		
		boolean[] broke = new boolean[n];
		
		while (incr < 2000000 && s >= 0 && s < n) {
			if (!broke[s] && a[s][0] == 1 && a[s][1] <= power) {
				ans++;
				broke[s] = true;
			}
			if (a[s][0] == 0) {
				power += a[s][1];
				dir *= -1;
			}
			
			s += power*dir;
			incr++;
		}
		
		out.print(ans);
		io.close();
		
	}
	
}
