public class LC106
{
	public static void main(String[] args)
	{
	}

	// 106. Construct Binary Tree from Inorder and Postorder Traversal
	static TreeNode buildTree(int[] inorder, int[] postorder)
	{
		int len = inorder.length;
		if (len == 0)
			return null;
		int val = postorder[len - 1];
		int index = len - 1;
		for (; index >= 0 && inorder[index] != val; index--) ;
        
		int[] leftInorder = new int[index];
		int[] leftPostorder = new int[index];
		int[] rightInorder = new int[len - index - 1];
		int[] rightPostorder = new int[len - index - 1];

		for (int i = 0; i < index; i++)
		{
			leftInorder[i] = inorder[i];
			leftPostorder[i] = postorder[i];
		}

		for (int i = index + 1; i < len; i++)
		{
			rightInorder[i - index - 1] = inorder[i];
			rightPostorder[i - index - 1] = postorder[i - 1];
		}

		TreeNode root = new TreeNode(val);
		root.left = buildTree(leftInorder, leftPostorder);
		root.right = buildTree(rightInorder, rightPostorder);
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
