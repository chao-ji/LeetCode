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
		Comparator<String[]> c = new MyComparator();
		Arrays.sort(tickets, c);
		list.add("JFK");
		recursive(list, "JFK", tickets);
		return list;
	}

	static boolean recursive(List<String> list, String begin, String[][] tickets)
	{
		if (list.size() == tickets.length + 1)
			return true;

		for (int i = 0; i < tickets.length; i++)
			if (!tickets[i][0].isEmpty() && tickets[i][0].equals(begin))
			{
				list.add(tickets[i][1]);
				String hold = tickets[i][0];
				tickets[i][0] = "";
				if (recursive(list, tickets[i][1], tickets))
					return true;
				else
				{
					tickets[i][0] = hold;
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
