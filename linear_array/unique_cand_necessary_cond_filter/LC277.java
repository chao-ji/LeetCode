public class LC277
{
	public static void main(String[] args)
	{
	}

	// 277. Find the Celebrity
	static int findCelebrity(int n)
	{
		int cand = 0;
		for (int i = 1; i < n; i++)
			if (knows(cand, i))
				cand = i;

		for (int i = 0; i < n; i++)
			if (i != cand && (!knows(i, cand) || knows(cand, i)))
				return -1;
		
		return cand;        
	}

	static boolean knows(int a, int b)
	{
		return false;
	}
}
