import java.util.*;

public class LC207
{
	public static void main(String[] args)
	{
	}

	// 207. Course Schedule
	static boolean canFinish(int numCourses, int[][] prerequisites)
	{
		int len = prerequisites.length;
		List<List<Integer>> edges = new ArrayList<List<Integer>>();
		Set<Integer> visited = new HashSet<Integer>();

		for (int i = 0; i < numCourses; i++)
			edges.add(new ArrayList<Integer>());
		for (int i = 0; i < len; i++)
			edges.get(prerequisites[i][0]).add(prerequisites[i][1]);
		for (int i = 0; i < numCourses; i++)
		{
			Set<Integer> cycle = new HashSet<Integer>();
			if (recursive(i, edges, visited, cycle) == false)
				return false;
		}

		return true;
	}

	static boolean recursive(int node, List<List<Integer>> edges, Set<Integer> visited, Set<Integer> cycle)
	{
		if (visited.contains(node))
			return true;
		if (cycle.contains(node))
			return false;

		cycle.add(node);
		for (int i = 0; i < edges.get(node).size(); i++)
			if (recursive(edges.get(node).get(i), edges, visited, cycle) == false)
				return false;
		visited.add(node);
		return true;
	}
}
