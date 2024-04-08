class Solution:
    def countStudents(self, student: List[int], sandwiches: List[int]) -> int:
        while sandwiches and sandwiches[0] in student:
            if student[0] == sandwiches[0]:
                student.pop(0)
                sandwiches.pop(0)
            else:
                current = student.pop(0)
                student.append(current)

        return len(student)