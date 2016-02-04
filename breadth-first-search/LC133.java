import java.util.*;

public class LC133
{
	public static void main(String[] args)
	{
	}

	// 133. Clone Graph
	static UndirectedGraphNode cloneGraph(UndirectedGraphNode node)
	{
		if (node == null)
			return null;
		Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
		Deque<UndirectedGraphNode> queue = new ArrayDeque<UndirectedGraphNode>();
		map.put(node, new UndirectedGraphNode(node.label));
		queue.addLast(node);
		while (!queue.isEmpty())
		{
			UndirectedGraphNode p = queue.removeFirst();
			for (int i = 0; i < p.neighbors.size(); i++)
			{
				UndirectedGraphNode q = p.neighbors.get(i);
				if (!map.containsKey(q))
				{
					map.put(q, new UndirectedGraphNode(q.label));
					queue.addLast(q);
				}
				else
					map.get(p).neighbors.add(map.get(q));
			}
		}
		return map.get(node);
	}	

	static class UndirectedGraphNode
	{
		int label;
		List<UndirectedGraphNode> neighbors;
		UndirectedGraphNode(int x)
		{
			label = x;
			neighbors = new ArrayList<UndirectedGraphNode>();
		}
	}
}
