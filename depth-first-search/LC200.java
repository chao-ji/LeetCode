public class LC200
{
	public static void main(String[] args)
	{
	}
	
	// 200. Number of Islands
	static int numIslands(char[][] grid)
	{
		int m = grid.length;
		if (m == 0)
			return 0;
		int n = grid[0].length;
		int count = 0;
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (grid[i][j] == '1')
				{
					mark(grid, i, j);
					count++;
				}
		return count;        
	}

	static void mark(char[][] grid, int i, int j)
	{
		grid[i][j] = '0';
		int m = grid.length;
		int n = grid[0].length;
		if (i > 0 && grid[i - 1][j] == '1')
			mark(grid, i - 1, j);
		if (j < n - 1 && grid[i][j + 1] == '1')
			mark(grid, i, j + 1);
		if (i < m - 1 && grid[i + 1][j] == '1')
			mark(grid, i + 1, j);
		if (j > 0 && grid[i][j - 1] == '1')
			mark(grid, i, j - 1);
	}
}
