using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _25179
	{
		void Main()
		{
			var str = Console.ReadLine().Split();
			var n = long.Parse(str[0]);
			var m = long.Parse(str[1]);

			if ((n - 1) % (m + 1) == 0)
				Console.WriteLine("Can't win");
			else
				Console.WriteLine("Can win");
		}
	}
}
