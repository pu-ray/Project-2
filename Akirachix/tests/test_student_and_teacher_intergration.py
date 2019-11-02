from django.test import TestCase

from student.models import Student

from teacher.models import Teacher

import datetime

class StudentTeacherTestCase(TestCase):
    def setUp(self):
        self.student_a = Student.objects.create(
            id="34678900",
            first_name = "Emmah",
            last_name = "Wanjiru",
            date_of_birth = datetime.date(1998,6,9),
            gender = "female",
            registration_no  = "9893",
            email = "emmahmbugua@gmail.com",
            phone_number = "0790773408",
            date_joined = datetime.date.today(),
            )

        # self.student_b = Student.objects.create(
        #     first_name = "Peter",
        #     last_name = "Kamau",
        #     date_of_birth = datetime.date(2007,4,7),
        #     gender = "male",
        #     registration_no  = "901",
        #     email = "kamaupeter@gmail.com",
        #     phone_number = "0720830673",
        #     date_joined = datetime.date.today(),
        #     )

        self.teacher_a = Teacher.objects.create(
        	first_name = "James",
            last_name = "Mwai",
            date_of_birth = datetime.date(1986,4,7),
            gender = "male",
            email = "stamatemwa@gmail.com",
            phone_number = "0745890760",
            proffessional="Software Developer",
            subject="Python",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )

        self.teacher_b = Teacher.objects.create(
        	first_name = "James",
            last_name = "Mwai",
            date_of_birth = datetime.date(1986,4,7),
            gender = "male",
            email = "stamatemwa@gmail.com",
            phone_number = "0745890760",
            proffessional="Software Developer",
            subject="Python",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )

# def test_teacher_can_teach_a_student(self):
#         self.teacher_a.students.add(self.student_a)
#         self.assertEqual(self.teacher_a.courses.count(),1)
#         self.teacher_a.courses.add(self.javascript)
#         self.assertEqual(self.teacher_a.courses.count(),2)
#         self.teacher_a.courses.add(self.design)
#         self.assertEqual(self.teacher_a.courses.count(),3)

#     def test_teacher_can_teach_many_courses(self):
#         self.teacher_a.courses.add(self.python,self.javascript,self.design)
#         self.assertEqual(self.teacher_a.courses.count(),3)