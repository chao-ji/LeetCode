public class LC105
{
	public static void main(String[] args)
	{
	}

	// 105. Construct Binary Tree from Preorder and Inorder Traversal
	static TreeNode buildTree(int[] preorder, int[] inorder)
	{
		int len = preorder.length;
		if (len == 0)
			return null;
		int val = preorder[0];
		int index = 0;
		for (; index < len && inorder[index] != val; index++) ;
		int[] leftPreorder = new int[index];
		int[] leftInorder = new int[index];
		int[] rightPreorder = new int[len - index - 1];
		int[] rightInorder = new int[len - index - 1];

		for (int i = 0; i < index; i++)
		{
			leftPreorder[i] = preorder[i + 1];
			leftInorder[i] = inorder[i];
		}

		for (int i = index + 1; i < len; i++)
		{
			rightPreorder[i - index - 1] = preorder[i];
			rightInorder[i - index - 1] = inorder[i];
		}

		TreeNode root = new TreeNode(val);
		root.left = buildTree(leftPreorder, leftInorder);
		root.right = buildTree(rightPreorder, rightInorder);
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
