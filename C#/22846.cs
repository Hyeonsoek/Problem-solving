using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_
{
	internal class _22846
	{
		class Dynamic
		{
			int k;
			int[,] cache;

			public Dynamic(int k)
			{
				this.k = k;
				cache = new int[2, k];

				for (int i = 0; i < 2; i++)
					for (int j = 0; j < k; j++)
						cache[i, j] = -1;
			}

			private struct State
			{
				public int V;
				public int R;
				public int Ret;
				public int CurrentDivisor;
				public bool IsFinished;

				public State(int v, int r)
				{
					V = v;
					R = r;
					Ret = r ^ 1;
					CurrentDivisor = 1;
					IsFinished = false;
				}
			}

			public int CalcNonRecursive(int initialV, int initialR)
			{
				Stack<State> stack = new Stack<State>();
				stack.Push(new State(initialV, initialR));

				while (stack.Count > 0)
				{
					State currentState = stack.Pop();

					if (currentState.V == k)
					{
						ProcessReturn(stack, currentState.R ^ 1);
						continue;
					}

					if (cache[currentState.R, currentState.V] != -1)
					{
						ProcessReturn(stack, cache[currentState.R, currentState.V]);
						continue;
					}

					for (int i = currentState.CurrentDivisor; i * i <= currentState.V; i++)
					{
						if (currentState.V % i > 0)
							continue;

						// 잠재적 다음 호출: v + i
						if (currentState.V + i <= k)
						{
							currentState.CurrentDivisor = i + 1;
							stack.Push(currentState);
							stack.Push(new State(currentState.V + i, currentState.R ^ 1));
							goto NextIteration;
						}

						// 잠재적 다음 호출: v + v/i
						if (currentState.V + currentState.V / i <= k)
						{
							currentState.CurrentDivisor = i + 1;
							stack.Push(currentState);
							stack.Push(new State(currentState.V + currentState.V / i, currentState.R ^ 1));
							goto NextIteration;
						}
					}

					cache[currentState.R, currentState.V] = currentState.Ret;
					ProcessReturn(stack, currentState.Ret);

				NextIteration:;
				}

				return cache[initialR, initialV];
			}

			private void ProcessReturn(Stack<State> stack, int returnValue)
			{
				if (stack.Count == 0) return; // 최종 종료

				State callerState = stack.Pop();

				if (returnValue == callerState.R)
				{
					cache[callerState.R, callerState.V] = callerState.R;
					ProcessReturn(stack, callerState.R);
				}
				else
				{
					stack.Push(callerState);
				}
			}
		}

		void Main()
		{
			var k = int.Parse(Console.ReadLine());
			Console.WriteLine(k == 2 || k == 6 ? "Kali" : "Ringo");
		}
	}
}
