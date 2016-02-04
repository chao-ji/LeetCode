public class LC114
{
	public static void main(String[] args)
	{
	}

	// 114. Flatten Binary Tree to Linked List
	static void flatten(TreeNode root)
	{
		if (root == null)
			return;
		flatten(root.left);
		TreeNode node = root.left;
		flatten(root.right);
		if (node == null)
			return;
		while (node.right != null)
			node = node.right;
		node.right = root.right;
		root.right = root.left;
		root.left = null;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
