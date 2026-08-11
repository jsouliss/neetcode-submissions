public class MyStack {
    private Queue<int> queue;
    private Queue<int> stack;

    public MyStack() {
        queue = new Queue<int>();
        stack = new Queue<int>();
    }
    
    public void Push(int x) {
        queue.Enqueue(x);
    }
    
    public int Pop() {
        int item;

        while (queue.Count > 1)
        {
            stack.Enqueue(queue.Dequeue());
        }
        item = queue.Dequeue();
        Queue <int> temp = queue; // empty
        queue = stack;
        stack = temp;

        return item;
    }
    
    public int Top() {
        int item;

        while (queue.Count > 1)
        {
            stack.Enqueue(queue.Dequeue());
        }
        item = queue.Dequeue();
        Queue<int> temp = queue;
        stack.Enqueue(item);
        queue = stack;
        stack = temp;
        
        return item;
    }
    
    public bool Empty() {
        return queue.Count == 0;
    }
}