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

		PriorityQueue<String> heap = new PriorityQueue<String>(k, new DataComparator());
		for (int i = 0; i < nums1.length; i++)
			heap.add(Integer.toString(nums1[i] + nums2[0]) + ":" + Integer.toString(i) + ":0");

		for (; k > 0 && !heap.isEmpty(); k--)
		{
			String[] csv = heap.poll().split(":");
			int i = Integer.parseInt(csv[1]);
			int j = Integer.parseInt(csv[2]);
			int[] pair = {nums1[i], nums2[j]};
			list.add(pair);

			if (j < nums2.length - 1)
				heap.add(Integer.toString(nums1[i] + nums2[j + 1]) + ":" + Integer.toString(i) + ":" + Integer.toString(j + 1));
		}

		return list;
	}

	static class DataComparator implements Comparator<String>
	{
		public int compare(String s1, String s2)
		{
			String[] csv1 = s1.split(":");
			String[] csv2 = s2.split(":");

			return Integer.parseInt(csv1[0]) - Integer.parseInt(csv2[0]);
		}
	}
}
