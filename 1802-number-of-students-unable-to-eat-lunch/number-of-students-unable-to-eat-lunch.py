from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwich: List[int]) -> int:
        student, sandwiches = deque(students), deque(sandwich)
        while sandwiches and sandwiches[0] in student:
            if student[0] == sandwiches[0]:
                student.popleft()
                sandwiches.popleft()
            else:
                current = student.popleft()
                student.append(current)

        return len(student)