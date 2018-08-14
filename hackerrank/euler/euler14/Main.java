import java.io.*;
import java.util.*;

public class Solution {
    
    private static int[] lengths = new int[5000001];
    
    private static void compute() {
        lengths[1] = 1;
        for (int i = 2; i < lengths.length; i++) {
            lengths[i] = collatz(i);
        } 
    }
    
    private static int collatz(long n) {
        if (n <= 5000000 && lengths[(int)n] > 0)
            return lengths[(int)n];
        if (n % 2 == 0) {
            int c = collatz(n / 2) + 1;
            if (n <= 5000000) lengths[(int)n] = c;
            return c;
        } else {
            int c = collatz(3 * n + 1) + 1;
            if (n <= 5000000) lengths[(int)n] = c;
            return c;
        }
    }

    public static void main(String[] args) {
        compute();
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        
        int max = 0, idx = 0;
        for (int i = 2; i < lengths.length; i++) {
            if (lengths[i] >= max) {
                max = lengths[i];
                idx = i;
                lengths[i] = i;
            } else
                lengths[i] = idx;
        }
        
        for (int i = 0; i < T; i++) {
            System.out.println(lengths[scan.nextInt()]);
        }
    }
}
