
class Solution:
    def countStudents(self, students, sandwiches):
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            elif students.count(0) == 0 or students.count(1) == 0:
                return len(students)
            else:
                students.append(students.pop(0))

        return 0
