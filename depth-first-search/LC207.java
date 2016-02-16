import java.util.*;

public class LC207
{
	public static void main(String[] args)
	{
	}

	// 207. Course Schedule
	static boolean canFinish(int numCourses, int[][] prerequisites)
	{
		List<List<Integer>> edges = new ArrayList<List<Integer>>();
		for (int i = 0; i < numCourses; i++)
			edges.add(new ArrayList<Integer>());
		for (int i = 0; i < prerequisites.length; i++)
			edges.get(prerequisites[i][0]).add(prerequisites[i][1]);

		boolean[] explored = new boolean[numCourses];
		for (int i = 0; i < numCourses; i++)
		{
			boolean[] path = new boolean[numCourses];
			if (!explored[i] && hasCycle(i, edges, path, explored))
				return false;
		}

		return true;
	}

	static boolean hasCycle(int root, List<List<Integer>> edges, boolean[] path, boolean[] explored)
	{
		if (explored[root] == true)
			return false;
		if (path[root] == true)
			return true;

		path[root] = true;
		for (int i = 0; i < edges.get(root).size(); i++)
			if (hasCycle(edges.get(root).get(i), edges, path, explored))
				return true;
		explored[root] = true;
		path[root] = false;

		return false;
	}
}
