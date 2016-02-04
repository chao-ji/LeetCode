public class LC108
{
	public static void main(String[] args)
	{
	}

	// 108. Convert Sorted Array to Binary Search Tree
	static TreeNode sortedArrayToBST(int[] nums)
	{
		if (nums.length == 0)
			return null;
		int mid = (nums.length - 1) / 2;
		int[] left = new int[mid];
		int[] right = new int[nums.length - mid - 1];
		for (int i = 0; i < mid; i++)
			left[i] = nums[i];
		for (int i = mid + 1; i < nums.length; i++)
			right[i - mid - 1] = nums[i];
		TreeNode root = new TreeNode(nums[mid]);
		root.left = sortedArrayToBST(left);
		root.right = sortedArrayToBST(right);
		return root;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
