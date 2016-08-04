import java.util.*;

public class LC373
{
	public static void main(String[] args)
	{
	}

	// 373. Find K Pairs with Smallest Sums (Isoform: LC23 Merge K Sorted Lists)
	public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k)
	{
		List<int[]> list = new ArrayList<int[]>();
		if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0)
			return list;
            
		PriorityQueue<Tuple> heap = new PriorityQueue<Tuple>();

		for (int i = 0; i < nums1.length; i++)
			heap.add(new Tuple(i, 0, nums1[i] + nums2[0]));
            
		for (; k > 0 && !heap.isEmpty(); k--)
		{
			Tuple tuple = heap.poll();
			int i = tuple.i;
			int j = tuple.j;
			int[] pair = {nums1[i], nums2[j]};
			list.add(pair);
            
			if (j < nums2.length - 1)
				heap.add(new Tuple(i, j + 1, nums1[i] + nums2[j + 1]));
		}
        
		return list;
	}

	static class Tuple implements Comparable<Tuple>
	{
		int i;
		int j;
		int val;
        
		Tuple(int i, int j, int val)
		{
			this.i = i;
			this.j = j;
			this.val = val;
		}
        
		public int compareTo(Tuple tuple)
		{
			return this.val - tuple.val;
		}
	}
}
