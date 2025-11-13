using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _9661
	{
		void Main()
		{
			var n = long.Parse(Console.ReadLine());
			Console.WriteLine((n % 5 == 0 || n % 5 == 2) ? "CY" : "SK");
		}

		void Dynamic()
		{
			var cache = new bool[1000001];
			cache[1] = cache[3] = true;
			for (int i = 4; i <= 1000000; i++)
			{
				for (int j = 0; Math.Pow(4, j) <= i; j++)
					cache[i] = !cache[i - (int)Math.Pow(4, j)];
			}

			for (int i = 1; i <= 100; i++)
				Console.WriteLine(i + " " + (cache[i] ? "SK" : "CY"));
		}
	}
}
