public class LC304
{
	public static void main(String[] args)
	{
	}

	// 304. Range Sum Query 2D - Immutable
	static class NumMatrix
	{
		int[][] cum; 
		public NumMatrix(int[][] matrix)
		{
			if (matrix.length == 0)
				return ;
			int m = matrix.length;
			int n = matrix[0].length;
			cum = new int[m][n];
			for (int i = 0; i < m; i++)
				for (int j = 0; j < n; j++)
					if (i == 0 && j == 0)
						cum[i][j] = matrix[i][j];
					else if (i == 0 && j != 0)
						cum[i][j] = matrix[i][j] + cum[i][j - 1];
					else if (i != 0 && j == 0)
						cum[i][j] = matrix[i][j] + cum[i - 1][j];
					else
						cum[i][j] = matrix[i][j] + cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1];
		}

		public int sumRegion(int row1, int col1, int row2, int col2)
		{
			if (cum == null)
				return 0;
			if (row1 == 0 && col1 == 0)
				return cum[row2][col2];
			else if (row1 == 0 && col1 != 0)
				return cum[row2][col2] - cum[row2][col1 - 1];
			else if (row1 != 0 && col1 == 0)
				return cum[row2][col2] - cum[row1 - 1][col2];
        
			return cum[row2][col2] - cum[row2][col1 - 1] - cum[row1 - 1][col2] + cum[row1 - 1][col1 - 1];
		}
	}
}
