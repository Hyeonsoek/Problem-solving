using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _2600
	{
		public class Program
		{
			void Main()
			{
				int[] bs = Console.ReadLine().Split().Select(value => int.Parse(value)).ToArray();

				int n = 501;
				bool[,] cache = new bool[n, n];

				for (int i = 0; i < n; i++)
					for (int j = 0; j < n; j++)
						for (int k = 0; k < 3; k++)
						{
							if (i >= bs[k] && !cache[i - bs[k], j])
								cache[i, j] |= true;

							if (j >= bs[k] && !cache[i, j - bs[k]])
								cache[i, j] |= true;
						}

				for (int i = 0; i < 5; i++)
				{
					string[] strs = Console.ReadLine().Split();
					int a = int.Parse(strs[0]);
					int b = int.Parse(strs[1]);
					Console.WriteLine(cache[a, b] ? "A" : "B");
				}
			}

			//static char Func(int[] bs, int a, int b)
			//{
			//	int[,,] cache = new int[2, a + 1, b + 1];
			//	for (int k =0; k < 2; k++)
			//		for (int i = 0; i < a + 1; i++)
			//			for (int j = 0; j < b + 1; j++)
			//				cache[k, i, j] = -1;

			//	return Dynamic(0, a, b, bs, ref cache) == 1 ? 'A' : 'B';
			//}

			//static int Dynamic(int index, int a, int b, int[] bs, ref int[,,] cache)
			//{
			//	if (a == 0 && b == 0)
			//		return index % 2;

			//	int v = index % 2;
			//	if (cache[v, a, b] != -1)
			//		return cache[v, a, b];

			//	if (v == 0)
			//	{
			//		int max = 0;
			//		for (int i = 0; i < bs.Length; i++)
			//		{
			//			if (bs[i] <= b) max = Math.Max(max, Dynamic(index + 1, a, b - bs[i], bs, ref cache));
			//			if (bs[i] <= a) max = Math.Max(max, Dynamic(index + 1, a - bs[i], b, bs, ref cache));
			//		}
			//		return cache[v, a, b] = max;
			//	}
			//	else
			//	{
			//		int min = 1;
			//		for (int i = 0; i < bs.Length; i++)
			//		{
			//			if (bs[i] <= b) min = Math.Min(min, Dynamic(index + 1, a, b - bs[i], bs, ref cache));
			//			if (bs[i] <= a) min = Math.Min(min, Dynamic(index + 1, a - bs[i], b, bs, ref cache));
			//		}
			//		return cache[v, a, b] = min;
			//	}
			//}
		}
	}
}
