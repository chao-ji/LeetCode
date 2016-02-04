public class LC124
{
	public static void main(String[] args)
	{
	}

	// 124. Binary Tree Maximum Path Sum
	static int maxPathSum(TreeNode root)
	{
		int[] max = new int[1];
		max[0] = Integer.MIN_VALUE;
		maxPathSum(root, max);
		return max[0];
	}

	static int maxPathSum(TreeNode root, int[] max)
	{
		if (root == null)
			return 0;
		int maxRootLeft = maxPathSum(root.left, max);
		int maxRootRight = maxPathSum(root.right, max);
		int maxRoot = Math.max(root.val, Math.max(root.val + maxRootLeft, root.val + maxRootRight));

		max[0] = Math.max(max[0], Math.max(maxRoot, root.val + maxRootLeft + maxRootRight));
		return maxRoot;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
