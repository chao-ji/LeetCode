public class PalindromeCounter 
{
	public static void main(String[] args)
	{
		String s = "hellolle";
		System.out.println(countPalindromes(s));
	}

	static int countPalindromes(String s)
	{
		int total = 0;
		if (s == null)
			return 0;
		else if (s.isEmpty())
			return 1;

		for (int i = 0; i < s.length(); i++)
		{
			int count = 0;
			int l = i;
			int h = i;
			while (l >= 0 && h <= s.length() - 1 && s.charAt(l) == s.charAt(h))
			{
				count++;
				l--;
				h++;
			}
			total += count;	

			if (i != s.length() - 1)
			{
				count = 0;
				l = i;
				h = i + 1;
				while (l >= 0 && h <= s.length() - 1 && s.charAt(l) == s.charAt(h))
				{
					count++;
					l--;
					h++;
				}
				total += count;
			}
		}

		return total;
	}
}
