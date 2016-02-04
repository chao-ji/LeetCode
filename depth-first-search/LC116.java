public class LC116
{
	public static void main(String[] args)
	{
	}

	// 116. Populating Next Right Pointers in Each Node
	static void connect(TreeLinkNode root)
	{
		if (root == null || root.left == null || root.right == null)
			return ;

		root.left.next = root.right;
		if (root.next != null)
			root.right.next = root.next.left;
		connect(root.left);
		connect(root.right);
	}

	static class TreeLinkNode
	{
		int val;
		TreeLinkNode left;
		TreeLinkNode right;
		TreeLinkNode next;
		TreeLinkNode(int x) { val = x; }
	}
}
