import java.util.*;

public class LC199
{
	public static void main(String[] args)
	{
	}

	// 199. Binary Tree Right Side View
	static List<Integer> rightSideView(TreeNode root)
	{
		List<Integer> list = new ArrayList<Integer>();
		if (root == null)
			return list;
		list.add(root.val);
		List<Integer> left = rightSideView(root.left);
		List<Integer> right = rightSideView(root.right);
		int i = 0;
		for (; i < right.size(); i++)
			list.add(right.get(i));
		for (; i < left.size(); i++)
			list.add(left.get(i));
		return list;    
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
