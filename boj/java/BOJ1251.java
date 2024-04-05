import java.io.*;
import java.util.*;

public class BOJ1251
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String string = br.readLine();
        int len = string.length();
        
        List<String> list = new ArrayList<>();
        for(int i = 1; i < len; i++)
        {
            for(int j = i+1 ; j < len; j++)
            {
                StringBuilder result = new StringBuilder();
                StringBuffer first = new StringBuffer(string.substring(0, i)).reverse();
                StringBuffer second = new StringBuffer(string.substring(i, j)).reverse();
                StringBuffer third = new StringBuffer(string.substring(j, len)).reverse();

                result.append(first.toString());
                result.append(second.toString());
                result.append(third.toString());

                list.add(result.toString());
            }
        }
        
        Collections.sort(list);
        System.out.println(list.get(0));
    }
}