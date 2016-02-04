import java.util.*;

public class LC93
{
	public static void main(String[] args)
	{
	}

	// 93. Restore IP Addresses
	static List<String> restoreIpAddresses(String s)
	{
		return restoreIpAddresses(s, 4);
	}

	static List<String> restoreIpAddresses(String s, int len)
	{
		List<String> list = new ArrayList<String>();
		if (s.isEmpty() || s.length() < len)
			return list;
		if (len == 1)
		{
			if (isValid(s))
				list.add(s);
			return list;
		}

		List<String> sub1 = restoreIpAddresses(s.substring(1), len - 1);
		for (int i = 0; i < sub1.size(); i++)
			list.add(s.substring(0, 1) + "." + sub1.get(i));
		if (s.length() >= 2 && isValid(s.substring(0, 2)))
		{
			List<String> sub2 = restoreIpAddresses(s.substring(2), len - 1);        
			for (int i = 0; i < sub2.size(); i++)
				list.add(s.substring(0, 2) + "." + sub2.get(i));
		}
		if (s.length() >= 3 && isValid(s.substring(0, 3)))
		{
			List<String> sub3 = restoreIpAddresses(s.substring(3), len - 1);
			for (int i = 0; i < sub3.size(); i++)
				list.add(s.substring(0, 3) + "." + sub3.get(i));
		}
		return list;
	}

	static boolean isValid(String s)
	{
		if (s.length() <= 3)
		{
			int val = Integer.parseInt(s);
			if (s.equals("0") || val >= 0 && val <= 255 && s.charAt(0) != '0')
			return true;
		}
		return false;
	}
}
