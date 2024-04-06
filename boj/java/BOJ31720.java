import java.io.*;
import java.util.*;

public class BOJ31720
{
    public static class Pair {
        int x, y;
        public Pair(int x, int y)
        {
            this.x = x; this.y = y;
        }    
    }

    final static Map<Character, Pair> dirr = new HashMap<>() {{
        put('U', new Pair(-1, 0));
        put('D', new Pair(1, 0));
        put('L', new Pair(0, -1));
        put('R', new Pair(0, 1));
    }};

    static int n;
    static int sx, sy, ex, ey;
    static String O, R;
    static String[] board;

    public static class State
    {
        int x, y, o, r;

        public State(int x, int y, int o, int r)
        {
            this.x = x;
            this.y = y;
            this.o = o;
            this.r = r;
        }
    }

    public static int Solve()
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if (board[i].charAt(j) == 'S') { sx = i; sy = j; }
                if (board[i].charAt(j) == 'E') { ex = i; ey = j; }
            }
        }
        
        int lenO = O.length();
        int lenR = R.length();
        boolean[][][][] visited = new boolean[lenR+1][lenO+1][n][n];
        visited[0][0][sx][sy] = true;

        Deque<State> queue = new ArrayDeque<>();
        queue.addFirst(new State(sx, sy, 0, 0));
        while(!queue.isEmpty())
        {
            State curr = queue.pop();

            if (curr.x == ex && curr.y == ey)
            { return curr.o + curr.r; }
            
            if (curr.o < lenO)
            {
                Pair d = dirr.get(O.charAt(curr.o));
                int xx = curr.x + d.x;
                int yy = curr.y + d.y;

                if ((xx < 0 || xx >= n || yy < 0 || yy >= n || board[xx].charAt(yy) == '#') 
                        && !visited[curr.r][curr.o + 1][curr.x][curr.y])
                {
                    visited[curr.r][curr.o + 1][curr.x][curr.y] = true;
                    queue.add(new State(curr.x, curr.y, curr.o + 1, curr.r));
                }
                
                if ((0 <= xx && xx < n && 0 <= yy && yy < n)
                        && board[xx].charAt(yy) != '#'
                        && !visited[curr.r][curr.o + 1][xx][yy])
                {
                    visited[curr.r][curr.o + 1][xx][yy] = true;
                    queue.add(new State(xx, yy, curr.o + 1, curr.r));
                }
            }

            if (curr.r < lenR)
            {
                Pair d = dirr.get(R.charAt(curr.r));
                int xx = curr.x + d.x;
                int yy = curr.y + d.y;

                if ((xx < 0 || xx >= n || yy < 0 || yy >= n || board[xx].charAt(yy) == '#') 
                        && !visited[curr.r + 1][curr.o][curr.x][curr.y])
                {
                    visited[curr.r + 1][curr.o][curr.x][curr.y] = true;
                    queue.add(new State(curr.x, curr.y, curr.o, curr.r + 1));
                }
                
                if ((0 <= xx && xx < n && 0 <= yy && yy < n)
                        && board[xx].charAt(yy) != '#'
                        && !visited[curr.r + 1][curr.o][xx][yy])
                {
                    visited[curr.r + 1][curr.o][xx][yy] = true;
                    queue.add(new State(xx, yy, curr.o, curr.r + 1));
                }
            }
        }

        return -1;
    }

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        board = new String[n];
        for(int i=0; i<n; i++)
        {
            board[i] = br.readLine();
        }
        
        O = br.readLine();
        R = br.readLine();

        System.out.println(Solve());
    }
}
