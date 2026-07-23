public class ListNode
{
    public int Value;
    public ListNode? Next;
    public ListNode? Prev;
    
    public ListNode(int val)
    {
        Value = val;
    }
}

public class MyLinkedList {

    private int size;
    private ListNode head;
    private ListNode tail;

    public MyLinkedList()
    {
        head = new ListNode(-1);
        tail = new ListNode(-1);
        head.Next = tail;
        tail.Prev = head;
        size = 0;
    }

    public int Get(int index)
    {
        if (index >= 0)
        {
            int i = 0;
            ListNode? curr = head.Next;
            while (curr != null && curr != tail)
            {
                if (i == index)
                {
                    return curr.Value;
                }
                i++;
                curr = curr.Next;
            }
        }
        return -1;
    }

    public void AddAtHead(int val)
    {
        ListNode newNode = new ListNode(val)
        {
            Prev = head,
            Next = head.Next
        };
        if (head.Next != null)
        {
            head.Next.Prev = newNode;
        }
        head.Next = newNode;
        size++;
    }

    public void AddAtTail(int val)
    {
        ListNode newNode = new ListNode(val)
        {
            Prev = tail.Prev,
            Next = tail
        };
        if (tail.Prev != null)
        {
            tail.Prev.Next = newNode;
        }
        tail.Prev = newNode;
        size++;
    }

    public void AddAtIndex(int index, int val)
    {
        if (index > size)
        {
            return;
        }
        ListNode curr = head;

        int i = 0;
        while (i < index)
        {
            i++;
            curr = curr.Next!;
        }

        ListNode newNode = new ListNode(val)
        {
            Prev = curr,
            Next = curr.Next
        };
        curr.Next!.Prev = newNode;
        curr.Next = newNode;
        size++;
    }

    public void DeleteAtIndex(int index)
    {
        if (index >= size)
        {
            return;
        }
        int i = 0;
        ListNode curr = head;
        while (i < index)
        {
            curr = curr.Next!;
            i++;
        }

        curr.Next!.Next!.Prev = curr;
        curr.Next = curr.Next.Next;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */