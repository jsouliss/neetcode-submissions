public class PageNode
{
    public string Value;
    public PageNode? Next;
    public PageNode? Prev;

    public PageNode(string val)
    {
        Value = val;
    }
}

public class BrowserHistory 
{
    private PageNode? curr;

    public BrowserHistory(string homepage)
    {
        curr = new PageNode(homepage);
    }
    
    public void Visit(string url)
    {
        PageNode newPageNode = new PageNode(url)
        {
            Prev = curr
        };
        curr!.Next = newPageNode;
        curr = newPageNode;
    }
    
    public string Back(int steps) 
    {
        int i = 0;
        while (curr!.Prev != null && i != steps)
        {
            curr = curr.Prev;
            i++;
        }
        return curr.Value;
    }
    
    public string Forward(int steps) 
    {
        int i = 0;
        while (curr!.Next != null && i != steps)
        {
            curr = curr.Next;
            i++;
        }
        return curr.Value;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.Visit(url);
 * string param_2 = obj.Back(steps);
 * string param_3 = obj.Forward(steps);
 */