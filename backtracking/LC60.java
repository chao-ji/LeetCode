import java.util.*;

public class LC60
{
	public static void main(String[] args)
	{
	}

	// 60. Permutation Sequence
	static String getPermutation(int n, int k)
	{
		int[] factorial = new int[n];
		List<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < n; i++)
		{
			factorial[i] = i == 0 ? 1 : factorial[i - 1] * (i + 1);
			list.add(i + 1);
		}
		k = k - 1;
		return recursive(list, factorial, k);
	}

	static String recursive(List<Integer> list, int[] factorial, int k)
	{
		if (list.size() == 1)
			return Integer.toString(list.get(0));
		int n = list.size();
		int index = k / factorial[n - 2];
		int d = list.get(index);
		list.remove(index);
		k = k % factorial[n - 2];
	
		return Integer.toString(d) + recursive(list, factorial, k);
	}
}
