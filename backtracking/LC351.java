public class LC351
{
	public static void main(String[] args)
	{
	}

	// 351. Android Unlock Patterns
	static int numberOfPatterns(int m, int n)
	{
		int rows = 3;
		int cols = 3;
		int val = 0;
		boolean[][] taken = new boolean[rows][cols];
		int[] x = {0, 0, 1};
		int[] y = {0, 1, 1};
		int[] nums = new int[3];
        
		for (int i = m; i <= n; i++)
		{
			int[] len = {i};

			for (int j = 0; j < 3; j++)
			{
				taken[x[j]][y[j]] = true;
				len[0]--;
				nums[j] = count(x[j], y[j], taken, len);
				len[0]++;
				taken[x[j]][y[j]] = false;
			}
            
			val += nums[0] * 4 + nums[1] * 4 + nums[2];            
		}
		return val;
	}

	static int count(int i, int j, boolean[][] taken, int[] len)
	{
		if (len[0] == 0)
			return 1;

		int rows = taken.length;
		int cols = taken[0].length;
		int val = 0;

		for (int x = 0; x < rows; x++)
			for (int y = 0; y < cols; y++)
				if ((x != i || y != j) && !taken[x][y])
				{
					if (x == i && Math.abs(y - j) == 2 && !taken[x][(y + j) / 2])
						continue;
					else if (y == j && Math.abs(x - i) == 2 && !taken[(x + i) / 2][y])
						continue;
					else if (Math.abs(x - i) == 2 && Math.abs(y - j) == 2 && !taken[(x + i) / 2][(y + j) / 2])
						continue;

					taken[x][y] = true;
					len[0]--;
					val += count(x, y, taken, len);
					len[0]++;
					taken[x][y] = false;
				}

		return val;
	}    	
}
