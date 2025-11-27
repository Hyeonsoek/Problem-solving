using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _24678
	{
		void Main()
		{
			var t = int.Parse(Console.ReadLine());
			var builder = new StringBuilder();
			while (t-- > 0)
			{
				var count = 0;
				var values = Console.ReadLine().Split().Select(v => int.Parse(v));

				foreach (var v in values)
					count += (v & 1);

				builder.AppendLine(count > 1 ? "B" : "R");
			}

			Console.Write(builder.ToString());
		}
	}
}
