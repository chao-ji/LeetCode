import java.util.*;

public class LC89
{
	public static void main(String[] args)
	{
	}

	// 89. Gray Code
	static List<Integer> grayCode(int n)
	{
		List<Integer> list = new ArrayList<Integer>();
		if (n < 2)
		{
			list.add(0);
			if (n == 0)
				return list;
			list.add(1);
			return list;
		}
		List<Integer> prev = grayCode(n - 1);
		list.addAll(prev);
		for (int i = prev.size() - 1; i >= 0; i--)
			list.add(prev.get(i) | 1 << (n - 1));
		return list;    
	}
}
