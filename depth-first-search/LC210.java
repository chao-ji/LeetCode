import java.util.*;

public class LC210
{
	public static void main(String[] args)
	{
	}

	// 210. Course Schedule II
	static int[] findOrder(int numCourses, int[][] prerequisites)
	{
		List<List<Integer>> edges = new ArrayList<List<Integer>>();
		for (int i = 0; i < numCourses; i++)
			edges.add(new ArrayList<Integer>());
		for (int i = 0; i < prerequisites.length; i++)
			edges.get(prerequisites[i][0]).add(prerequisites[i][1]);

		boolean[] explored = new boolean[numCourses];
		Deque<Integer> stack = new ArrayDeque<Integer>();
		for (int i = 0; i < numCourses; i++)
		{
			boolean[] path = new boolean[numCourses];
			if (!explored[i] && hasCycle(i, edges, path, explored, stack))
				return new int[0];
		}

		int i = 0;
		int[] order = new int[numCourses];
		while (!stack.isEmpty())
			order[i++] = stack.removeFirst();
		return order;
	}

	static boolean hasCycle(int root, List<List<Integer>> edges, boolean[] path, boolean[] explored, Deque<Integer> stack)
	{
		if (explored[root] == true)
			return false;
		if (path[root] == true)
			return true;

		path[root] = true;
		for (int i = 0; i < edges.get(root).size(); i++)
			if (hasCycle(edges.get(root).get(i), edges, path, explored, stack))
		return true;

		explored[root] = true;
		path[root] = false;
		stack.addLast(root);

		return false;
	}
}
