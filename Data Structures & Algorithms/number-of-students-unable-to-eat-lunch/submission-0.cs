public class Solution {
    public int CountStudents(int[] students, int[] sandwiches) {
        int i = 0;
        int j = 0;
        Queue<int> qStudents = new Queue<int>(students);

        while (j != qStudents.Count)
        {
            if (qStudents.Peek() == sandwiches[i])
            {
                qStudents.Dequeue();
                j = 0; // reset counter 
                i++;
            }
            else
            {
                int frontStudent = qStudents.Dequeue();
                qStudents.Enqueue(frontStudent);
                j++;
            }
        }

        return qStudents.Count();
    }
}