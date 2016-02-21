public class LC276
{
	public static void main(String[] args)
	{
	}

	// 276. Paint Fence
	static int numWays(int n, int k)
	{
		if (n == 0 || k == 0)
			return 0;

		if (n == 1)
			return k;
		else if (n == 2)
			return k * k;
		else if (n == 3)
			return k * k * k - k;

		int a_1 = k * k * k - k;
		int a_2 = k * k;
		int a_3 = k;
		int val = 0;

		for (int i = 4; i <= n; i++)
		{
			val = a_1 * k  - a_3 * (k - 1);
			a_3 = a_2;
			a_2 = a_1;
			a_1 = val;            
		}   
		return val;
	}
}
