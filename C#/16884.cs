using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
    class _16884
    {
		void Main()
		{
			int t = int.Parse(Console.ReadLine());
			while (t-- > 0)
			{
				Console.WriteLine(int.Parse(Console.ReadLine()) % 2 == 0 ? "cubelover" : "koosaga");
			}
		}
	}
}
