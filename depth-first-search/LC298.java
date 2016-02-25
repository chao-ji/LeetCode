public class LC298
{
	public static void main(String[] args)
	{
	}

	// 298. Binary Tree Longest Consecutive Sequence
	static int longestConsecutive(TreeNode root)
	{
		int[] len = new int[1];
		len[0] = 0;
		recursive(root, len);
		return len[0];
	}

	static int recursive(TreeNode root, int[] len)
	{
		if (root == null)
			return 0;

		int left = recursive(root.left, len);
		int right = recursive(root.right, len);
		int max = 1;
		if (root.left != null && root.left.val == root.val + 1)
			max = left + 1;
		if (root.right != null && root.right.val == root.val + 1)
			max = Math.max(max, right + 1);

		len[0] = Math.max(len[0], max);
		return max;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
