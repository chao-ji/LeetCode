import java.util.*;

public class LC332
{
	public static void main(String[] args)
	{
	}

	// 332. Reconstruct Itinerary
	static List<String> findItinerary(String[][] tickets)
	{
		List<String> list = new ArrayList<String>();
		if (tickets.length == 0)
			return list;
		boolean[] taken = new boolean[tickets.length];
		Comparator<String[]> c = new MyComparator();
		Arrays.sort(tickets, c);
		list.add("JFK");
		recursive(list, "JFK", taken, tickets);
		return list;
	}

	static boolean recursive(List<String> list, String begin, boolean[] taken, String[][] tickets)
	{
		if (list.size() == tickets.length + 1)
			return true;

		for (int i = 0; i < tickets.length; i++)
			if (taken[i] == false && tickets[i][0].equals(begin))
			{
				list.add(tickets[i][1]);
				taken[i] = true;
				if (recursive(list, tickets[i][1], taken, tickets))
					return true;
				else
				{
					taken[i] = false;
					list.remove(list.size() - 1);
				}
			}
		return false;    
	}

	static class MyComparator implements Comparator<String[]>
	{
		public int compare(String[] s1, String[] s2)
		{
			if (!s1[0].equals(s2[0]))
				return s1[0].compareTo(s2[0]);
			return s1[1].compareTo(s2[1]);
		}
	}
}
