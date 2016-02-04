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

		Deque<Integer> stack = new ArrayDeque<Integer>();
		Set<Integer> visited = new HashSet<Integer>();

		for (int i = 0; i < numCourses; i++)
		{
			HashSet<Integer> cycle = new HashSet<Integer>();
			if (recursive(i, edges, visited, cycle, stack) == false)
				return new int[0];
		}
		int[] order = new int[numCourses];
		int i = 0;
		while (!stack.isEmpty())
			order[i++] = stack.removeFirst();
		return order;    
	}

	static boolean recursive(int node, List<List<Integer>> edges, Set<Integer> visited, Set<Integer> cycle, Deque<Integer> stack)
	{
		if (visited.contains(node))
			return true;
		if (cycle.contains(node))
			return false;
		cycle.add(node);    

		for (int i = 0; i < edges.get(node).size(); i++)
			if (recursive(edges.get(node).get(i), edges, visited, cycle, stack) == false)
				return false;
		visited.add(node);
		stack.addLast(node);
		return true;
	}
}
