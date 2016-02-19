public java.util.*;
public class LC146
{
	public static void main(String[] args)
	{
	}
}

class LRUCache
{
	int size;
	int count;
	LinkedListNode head;
	LinkedListNode tail;
	Map<Integer, Integer> hash;
	Map<Integer, LinkedListNode> pointer;

	public LRUCache(int capacity)
	{
		size = capacity;
		count = 0;
		hash = new HashMap<Integer, Integer>();
		pointer = new HashMap<Integer, LinkedListNode>();
	}

	public int get(int key)
	{
		if (!hash.containsKey(key))
			return -1;
		touch(pointer.get(key));
		return hash.get(key);
	}

	public void set(int key, int value)
	{
		if (count < size)
		{
			if (!hash.containsKey(key))
			{
				LinkedListNode p = new LinkedListNode(key);
				hash.put(key, value);
				pointer.put(key, p);
				if (count == 0)
					head = p;
				else
				{
					tail.tail = p;
					p.head = tail;
				}
				tail = p;
				count++;
			}
			else
			{
				hash.put(key, value);
				touch(pointer.get(key));
			}
		}
		else
		{
			if (count == 0)
				return ;
			if (!hash.containsKey(key))
			{
				hash.remove(head.val);
				pointer.remove(head.val);
				LinkedListNode p = new LinkedListNode(key);
				tail.tail = p;
				head = head.tail;
				head.head = null;
				p.head = tail;
				tail = p;

				hash.put(key, value);
				pointer.put(key, p);
			}
			else
			{
				touch(pointer.get(key));
				hash.put(key, value);
			}
		}
	}

	public void touch(LinkedListNode p)
	{
		if (p.tail == null)
			return ;
		if (p.head != null)
		{
			p.head.tail = p.tail;
			p.tail.head = p.head;
		}
		else
		{
			head = p.tail;
			p.tail.head = null;
		}
		tail.tail = p;
		p.head = tail;
		p.tail = null;
		tail = p;
	}

	static class LinkedListNode
	{
		LinkedListNode head;
		LinkedListNode tail;
		int val;
		LinkedListNode(int x) {val = x;}
	}
}
