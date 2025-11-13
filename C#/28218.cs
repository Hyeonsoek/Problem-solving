using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _28218
	{
		public class Dynamic
		{
			public int n, m, k;
			public int[,] cache;
			public string[] board;

			public Dynamic(int n, int m, int k, string[] board)
			{
				this.n = n;
				this.m = m;
				this.k = k;
				this.board = board;

				cache = new int[m, n];
				for (int i = 0; i < m; i++)
					for (int j = 0; j < n; j++)
						cache[i, j] = -1;
			}

			public int GetValue(int x, int y)
			{
				if (x == m - 1 && y == n - 1)
					return 1;

				if (cache[x, y] != -1)
					return cache[x, y];

				int ret = 1;
				if (x + 1 < m && board[y][x + 1] == '.')
					ret = Math.Min(ret, 1 ^ GetValue(x + 1, y));

				if (y + 1 < n && board[y + 1][x] == '.')
					ret = Math.Min(ret, 1 ^ GetValue(x, y + 1));

				for (int i = 1; i <= k; i++)
				{
					if (x + i < m && y + i < n && board[y + i][x + i] == '.')
						ret = Math.Min(ret, 1 ^ GetValue(x + i, y + i));
				}

				return cache[x, y] = ret;
			}
		}

		void Main()
		{
			var values = Console.ReadLine().Split();
			int n = int.Parse(values[0]), m = int.Parse(values[1]), k = int.Parse(values[2]);

			var board = new string[n];
			for (int i = 0; i < n; i++)
				board[i] = Console.ReadLine();

			var d = new Dynamic(n, m, k, board);

			int q = int.Parse(Console.ReadLine());
			for (int i = 0; i < q; i++)
			{
				var pair = Console.ReadLine().Split();
				int y = int.Parse(pair[0]);
				int x = int.Parse(pair[1]);
				Console.WriteLine(d.GetValue(x - 1, y - 1) == 0 ? "First" : "Second");
			}
		}
	}
}
