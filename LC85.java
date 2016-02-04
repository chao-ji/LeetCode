import java.util.*;

public class LC85
{
	public static void main(String[] args)
	{
	}

	// 85. Maximal Rectangle
	static int maximalRectangle(char[][] matrix)
	{
		int m = matrix.length;
		if (m == 0)
			return 0;
		int n = matrix[0].length;
		int max = 0;

		int[] height = new int[n];
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
				if (matrix[i][j] == '1')
					height[j]++;
				else
					height[j] = 0;

			List<Integer> list = new ArrayList<Integer>();
			Deque<Integer> stack = new ArrayDeque<Integer>();
			for (int j = 0; j < n; j++)
				list.add(height[j]);
			list.add(0);
            
			for (int j = 0; j < list.size(); j++)
				if (stack.isEmpty() || height[stack.peekLast()] < list.get(j))
					stack.addLast(j);
				else
				{
					int y = list.get(stack.removeLast());
					int left = !stack.isEmpty() ? stack.peekLast() + 1 : 0;
					max = max < (j - left) * y ? (j - left) * y : max;
					j--;
				}
		}
        
		return max;
	}
}
