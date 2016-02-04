public class LC109
{
	public static void main(String[] args)
	{
	}

	// 109. Convert Sorted List to Binary Search Tree
	static TreeNode sortedListToBST(ListNode head)
	{
		if (head == null)
			return null;
		else if (head.next == null)
			return new TreeNode(head.val);

		ListNode p = head;
		ListNode q = head.next;
		while (q.next != null)
		{
			q = q.next;
			p = p.next;
			if (q.next != null)
				q = q.next;
		}
		TreeNode root = new TreeNode(p.val);
		root.right = sortedListToBST(p.next);
		if (p == head)
			root.left = null;
		else
		{
			for (q = head; q.next != p; q = q.next) ;
			q.next = null;
			root.left = sortedListToBST(head);
		}
		return root;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}

	static class ListNode
	{
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
}
