using System;
using System.Linq;

namespace C_
{
	internal class _11062
	{
		public class Program
		{
			void Main()
			{
				int t = int.Parse(Console.ReadLine());
				for (int i = 0; i < t; i++)
				{
					int n = int.Parse(Console.ReadLine());
					int[] cards = Console.ReadLine().Split().Select(value => int.Parse(value)).ToArray();
					Console.WriteLine(Card(n, cards));
				}
			}

			int Card(int n, int[] cards)
			{
				int[,] cache = new int[n, n];
				for (int i = 0; i < n; i++)
					for (int j = 0; j < n; j++)
						cache[i, j] = -1;

				return Dynamic(ref cache, cards, 0, 0, n - 1);
			}

			int Dynamic(ref int[,] cache, int[] cards, int num, int left, int right)
			{
				if (left > right)
					return 0;

				if (cache[left, right] != -1)
					return cache[left, right];

				if (num % 2 == 0)
					return cache[left, right] = Math.Max(
							cards[left] + Dynamic(ref cache, cards, num + 1, left + 1, right),
							cards[right] + Dynamic(ref cache, cards, num + 1, left, right - 1)
						);

				return cache[left, right] = Math.Min(
						Dynamic(ref cache, cards, num + 1, left + 1, right),
						Dynamic(ref cache, cards, num + 1, left, right - 1)
					);
			}
		}
	}
}
