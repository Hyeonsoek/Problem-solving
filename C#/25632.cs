using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _25632
	{
		void Main()
		{
			var isPrime = Enumerable.Repeat(true, 1100).ToArray();
			isPrime[0] = isPrime[1] = false;

			for (int i = 2; i <= 1000; i++)
			{
				if (isPrime[i])
				{
					for (int j = i * i; j <= 1000; j += i)
						isPrime[j] = false;
				}
			}

			var yt = Console.ReadLine().Split();
			var yj = Console.ReadLine().Split();

			int a = int.Parse(yt[0]), b = int.Parse(yt[1]);
			int c = int.Parse(yj[0]), d = int.Parse(yj[1]);

			int e = Math.Max(a, c), f = Math.Min(b, d);

			int l = 0, m = 0, r = 0;

			for (int i = a; i <= b; i++)
				if (isPrime[i])
					l++;

			for (int i = c; i <= d; i++)
				if (isPrime[i])
					r++;

			for (int i = e; i <= f; i++)
				if (isPrime[i])
					m++;

			int count = 0;
			while (!((l == 0 || r == 0) && (m == 0)))
			{
				if (count % 2 == 0)
				{
					if (m > 0)
					{
						l--; m--; r--;
					}
					else l--;
				}
				else
				{
					if (m > 0)
					{
						l--; m--; r--;
					}
					else r--;
				}

				count++;
			}

			if (l == 0 && m == 0)
				Console.WriteLine("yj");
			else
				Console.WriteLine("yt");
		}
	}
}
