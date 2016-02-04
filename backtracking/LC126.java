import java.util.*;

public class LC126
{
	public static void main(String[] args)
	{
	}

	// 126. Word Ladder II	
	static List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList)
	{
		List<List<String>> paths = new ArrayList<List<String>>();
		if (beginWord.isEmpty() || endWord.isEmpty())
			return paths;

		wordList.add(endWord);
		Deque<String> queue = new ArrayDeque<String>();
		Map<String, Integer> dist = new HashMap<String, Integer>();
		Map<String, List<String>> desc = new HashMap<String, List<String>>();
		queue.addLast(beginWord);
		dist.put(beginWord, 0);
		while (!queue.isEmpty())
		{
			String curr = queue.removeFirst();
			List<String> children = new ArrayList<String>();
			char[] array = curr.toCharArray();
			for (int i = 0; i < array.length; i++)
			{
				char hold = array[i];
				for (char j = 'a'; j <= 'z'; j++)
				{
					if (j == array[i])
						continue;
					array[i] = j;
					String next = new String(array);
					if (wordList.contains(next))
						if (!dist.containsKey(next))
						{
							queue.addLast(next);
							dist.put(next, dist.get(curr) + 1);
							children.add(next);
						}
						else if (dist.get(next) == dist.get(curr) + 1)
							children.add(next);	
				}
				array[i] = hold;
			}
			desc.put(curr, children);
		}
		List<String> path = new ArrayList<String>();
		path.add(beginWord);
		if (dist.containsKey(endWord))
			recursive(paths, desc, path, endWord, dist.get(endWord));
		return paths;
	}

	static void recursive(List<List<String>> paths, Map<String, List<String>> desc, List<String> path, String end, int dist)
	{
		if (path.isEmpty())
			return ;
		if (path.size() - 1 == dist)
		{
			if  (path.get(path.size() - 1).equals(end))
			{
				paths.add(new ArrayList<String>());
				paths.get(paths.size() - 1).addAll(path);
			}
			path.remove(path.size() - 1);
			return ;
		}

		List<String> children = desc.get(path.get(path.size() - 1));
		for (int i = 0; i < children.size(); i++)
		{
			path.add(children.get(i));
			recursive(paths, desc, path, end, dist); 
		}
		path.remove(path.size() - 1);
	}
}
