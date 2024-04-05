import java.io.*;
import java.util.*;

public class BOJ11652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<Long, Integer> dict = new HashMap<>();

        long n = Long.parseLong(br.readLine());
        for (int i = 0; i < n; i++) {
            long card = Long.parseLong(br.readLine());
            dict.put(card, dict.getOrDefault(card, 0) + 1);
        }

        int count = 0;
        long result = Long.MAX_VALUE;

        for(Map.Entry<Long, Integer> entry : dict.entrySet()) {
            int value = entry.getValue();
            long key = entry.getKey();

            if (count <= value)
            {
                result = count == value ? Math.min(result, key) : key;
                count = value;
            }
        }

        System.out.println(result);
    }
}
