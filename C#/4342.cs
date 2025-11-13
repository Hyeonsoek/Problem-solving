using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _4342
	{

		public class Program
		{
			void Main()
			{
				while (true)
				{
					var str = Console.ReadLine().Split(' ');
					var a = long.Parse(str[0]);
					var b = long.Parse(str[1]);
					if (a == 0 && b == 0)
						break;

					Console.WriteLine((GCD(a, b) ? "A" : "B") + " wins");
				}
			}

			bool GCD(long a, long b)
			{
				if (a < b)
					return GCD(b, a);

				if (a % b == 0)
					return true;

				if (a < b * 2)
					return !GCD(b, a % b);
				return true;
			}
		}
	}
}
