import java.util.*;

public class LC52
{
	public static void main(String[] args)
	{
	}

	// 52. N-Queens II
	static int totalNQueens(int n)
	{
		int[] count = new int[1];
		count[0] = 0;
		List<Integer> list = new ArrayList<Integer>();
		recursive(count, list, n);
		return count[0];
	}

	static void recursive(int[] count, List<Integer> list, int n)
	{
		if (list.size() == n)
		{
			count[0]++;
			list.remove(list.size() - 1);
			return;
		}
		for (int i = 0; i < n; i++)
		{
			boolean isValid = true;
			int x1 = list.size();
			int y1 = i;
			for (int j = 0; j < list.size(); j++)
			{
				int x2 = j;
				int y2 = list.get(j);
				if (y1 == y2 || Math.abs(x1 - x2) == Math.abs(y1 - y2))
				{
					isValid = false;
					break;
				}
			}
			if (isValid)
			{
				list.add(i);
				recursive(count, list, n);
			}
		}
		if (!list.isEmpty())
			list.remove(list.size() - 1);
	}
}
