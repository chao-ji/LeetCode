import java.util.*;

public class LC84
{
	public static void main(String[] args)
	{
	}

	// 84. Largest Rectangle in Histogram
	static int largestRectangleArea(int[] height)
	{
		List<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < height.length; i++)
			list.add(height[i]);
		list.add(0);
        
		int max = 0;
		Deque<Integer> stack = new ArrayDeque<Integer>();
        
		for (int i = 0; i < list.size(); i++)
			if (stack.isEmpty() || list.get(stack.peekLast()) < list.get(i))
				stack.addLast(i);
			else
			{
				int y = list.get(stack.removeLast());
				int left = !stack.isEmpty() ? (stack.peekLast() + 1) : 0;
				max = max < (i - left) * y ? (i - left) * y : max;
				i--;
			}
		return max;    
	}
}
