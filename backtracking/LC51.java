import java.util.*;

public class LC51
{
	public static void main(String[] args)
	{
		System.out.println(solveNQueens(5));
	}

	// 51. N-Queens
	static List<List<String>> solveNQueens(int n)
	{
		List<List<String>> nqueens = new ArrayList<List<String>>();
		List<Integer> list = new ArrayList<Integer>();
		recursive(nqueens, list, n);
		return nqueens;
	}

	static void recursive(List<List<String>> nqueens, List<Integer> list, int n)
	{
		if (list.size() == n)
		{
			List<String> board = new ArrayList<String>();
			for (int i = 0; i < n; i++)
			{
				StringBuilder row = new StringBuilder();
				for (int j = 0; j < n; j++)
					row.append(list.get(i) == j ? "Q" : ".");
				board.add(row.toString());
			}
			nqueens.add(board);
			list.remove(list.size() - 1);
			return ;
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
				recursive(nqueens, list, n);
			}
		}
		if (!list.isEmpty())
			list.remove(list.size() - 1);
	}
}
