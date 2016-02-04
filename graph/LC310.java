import java.util.*;

public class LC310
{
	public static void main(String[] args)
	{
	}

	// 310. Minimum Height Trees
	static List<Integer> findMinHeightTrees(int n, int[][] edges)
	{
		List<Integer> list = new ArrayList<Integer>();
		List<List<Integer>> adj = new ArrayList<List<Integer>>();
		for (int i = 0; i < n; i++)
			adj.add(new ArrayList<Integer>());
		for (int i = 0; i < edges.length; i++)
		{
			adj.get(edges[i][0]).add(edges[i][1]);
			adj.get(edges[i][1]).add(edges[i][0]);
		}
		for (int i = 0; i < n; i++)
			if (adj.get(i).size() == 1)
				list.add(i);
		int size = n;        
		while (n > 2)
		{
			n -= list.size();
			List<Integer> hold = new ArrayList<Integer>();
			for (int i = 0; i < list.size(); i++)
			{
				int next = adj.get(list.get(i)).get(0);
				adj.get(next).remove(list.get(i));
				if (adj.get(next).size() == 1)
					hold.add(next);
			}
			list = hold;        
		}
		if (size == 1)
			list.add(0);
        	
		return list;
	}
}
