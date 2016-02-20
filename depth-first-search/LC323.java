import java.util.*;

public class LC323
{
	public static void main(String[] args)
	{
	}

	// 323. Number of Connected Components in an Undirected Graph
	static int countComponents(int n, int[][] edges)
	{
		List<List<Integer>> adj = new ArrayList<List<Integer>>();
		boolean[] explored = new boolean[n];

		for (int i = 0; i < n; i++)
			adj.add(new ArrayList<Integer>());
		for (int i = 0; i < edges.length; i++)
		{
			adj.get(edges[i][0]).add(edges[i][1]);
			adj.get(edges[i][1]).add(edges[i][0]);
		}

		int count = 0;
		for (int i = 0; i < n; i++)
		{
			boolean[] path = new boolean[n];
			if (!explored[i])
			{
				depthFirstSearch(i, adj, path, explored);
				count++;
			}
		}

		return count;
	}

	static void depthFirstSearch(int root, List<List<Integer>> adj, boolean[] path, boolean[] explored)
	{
		if (path[root] == true || explored[root] == true)
			return ;

		path[root] = true;
		for (int i = 0; i < adj.get(root).size(); i++)
			depthFirstSearch(adj.get(root).get(i), adj, path, explored);
		explored[root] = true;
		path[root] = false;
	}
}
