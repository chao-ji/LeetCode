import java.util.*;

public class LC269
{
	public static void main(String[] args)
	{
	}

	// 269. Alian Dictionary
	static String alienOrder(String[] words)
	{
		Set<Character> alphabet = new HashSet<Character>();
		List<List<Integer>> edges = new ArrayList<List<Integer>>();

		for (int i = 0; i < words.length; i++)
			for (int j = 0; j < words[i].length(); j++)
				if (!alphabet.contains(words[i].charAt(j)))
					alphabet.add(words[i].charAt(j));

		for (int i = 0; i < 26; i++)
			edges.add(new ArrayList<Integer>());

		for (int i = 0; i < words.length - 1; i++)
		{
			int j = 0;
			for (; j < Math.min(words[i].length(), words[i + 1].length()); j++)
				if (words[i].charAt(j) != words[i + 1].charAt(j))
					break;

			if (j < Math.min(words[i].length(), words[i + 1].length()))
			{
				int c = (int) (words[i].charAt(j) - 'a');
				int d = (int) (words[i + 1].charAt(j) - 'a');
				edges.get(c).add(d);
			}
		}

		boolean[] explored = new boolean[26];
		Deque<Integer> stack = new ArrayDeque<Integer>();
		for (int i = 0; i < 26; i++)
			if (alphabet.contains((char) (i + 'a')))
			{
				boolean[] path = new boolean[26];
				if (!explored[i] && hasCycle(i, edges, path, explored, stack))
					return new String();
			}

		int i = 0;
		StringBuilder order = new StringBuilder();
		while (!stack.isEmpty())
			order.append((char) (stack.removeLast() + 'a'));

		return order.toString();
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
