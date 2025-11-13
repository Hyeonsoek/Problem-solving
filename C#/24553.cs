using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _24553
	{
		void Main()
		{
			int t = int.Parse(Console.ReadLine());
			for (int i = 0; i < t; i++)
			{
				long n = long.Parse(Console.ReadLine());
				Console.WriteLine((n % 10 == 0) ? 0 : 1);
			}
		}

		void Dynamic()
		{
			var palins = new List<long>();
			var cache = new bool[1000001];

			for (int i = 1; i < 10; i++)
			{
				cache[i] = true;
				palins.Add(i);
			}

			for (long i = 10; i <= 1000000; i++)
			{
				if (IsPalindrom(i))
					palins.Add(i);

				foreach (var palin in palins)
					cache[i] |= !cache[i - palin];
			}
		}

		bool IsPalindrom(long n)
		{
			string str = n.ToString();
			for (int i = 0; i < str.Length / 2; i++)
			{
				if (str[i] != str[str.Length - i - 1])
					return false;
			}

			return true;
		}
	}
}
