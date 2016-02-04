public class LC98
{
	public static void main(String[] args)
	{
	}

	// 98. Validate Binary Search Tree
	static boolean isValidBST(TreeNode root)
	{
		if (root == null)
			return true;

		int leftMax = Integer.MIN_VALUE;
		TreeNode node = root.left;
		if (node != null)
		{
			while (node.right != null)
				node = node.right;
			leftMax = leftMax < node.val ? node.val : leftMax;        
		}

		int rightMin = Integer.MAX_VALUE;
		node = root.right;
		if (node != null)
		{
			while (node.left != null)
				node = node.left;
			rightMin = rightMin > node.val ? node.val : rightMin;        
		}
		return isValidBST(root.left) && isValidBST(root.right) && (root.left == null || leftMax < root.val) && (root.right == null || rightMin > root.val);
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
