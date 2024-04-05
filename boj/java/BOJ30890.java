import java.io.*;
import java.util.*;

public class BOJ30890 {
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int lca = x * y;

        int[] arr = new int[lca+1];

        for(int i=x; i<=lca; i+=x)
            arr[i] += 2;

        for(int i=y; i<=lca; i+=y)
            arr[i] += 1;

        StringBuilder result = new StringBuilder();
        for(int i=0; i<=lca; i++)
            if (arr[i] > 0)
                result.append(arr[i]);

        System.out.println(result);
    }
}