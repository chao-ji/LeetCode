import java.util.*;

public class LC257
{
	public static void main(String[] args)
	{
	}

	// 257. Binary Tree Paths
	static List<String> binaryTreePaths(TreeNode root)
	{
		List<String> paths = new ArrayList<String>();
		if (root == null)
			return paths;
		List<TreeNode> path = new ArrayList<TreeNode>();
		path.add(root);
		StringBuilder s = new StringBuilder();
		s.append(Integer.toString(root.val));
		recursive(paths, path, s);
		return paths;
	}

	static void recursive(List<String> paths, List<TreeNode> path, StringBuilder s)
	{
		if (path.isEmpty())
			return ;
		TreeNode node = path.get(path.size() - 1);
		if (node.left == null && node.right == null)
		{
			paths.add(s.toString());
			int i = s.length() - 1;
			for (; i > 0 && s.charAt(i) != '>'; i--);
			i = i > 0 ? i - 1 : i;
			s.delete(i, s.length());
			path.remove(path.size() - 1);
			return ;
		}
		if (node.left != null)
		{
			path.add(node.left);
			s.append("->" + Integer.toString(node.left.val));
			recursive(paths, path, s);
		}
		if (node.right != null)
		{
			path.add(node.right);
			s.append("->" + Integer.toString(node.right.val));
			recursive(paths, path, s);
		}
		int i = s.length() - 1;
		for (; i > 0 && s.charAt(i) != '>'; i--);
		i = i > 0 ? i - 1 : i;
		s.delete(i, s.length());
		path.remove(path.size() - 1);
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
