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

		boolean[] visited = new boolean[numCourses];    
		for (int i = 0; i < numCourses; i++)
		{
			Set<Integer> path = new HashSet<Integer>();
			if (!visited[i] && hasCycle(i, edges, path, visited))
				return false;
		}
		return true;
	}

	static boolean hasCycle(int root, List<List<Integer>> edges, Set<Integer> path, boolean[] visited)
	{
		visited[root] = true;
		if (path.contains(root))
			return true;
		path.add(root);
		for (int i = 0; i < edges.get(root).size(); i++)
			if (hasCycle(edges.get(root).get(i), edges, path, visited))
				return true;
		path.remove(root);
		return false;        
	}
}
