from django.test import TestCase

from teacher.models import Teacher

from course.models import Course

import datetime

class TeacherCourseTestCase(TestCase):
    def setUp(self):
            self.teacher_a = Teacher.objects.create(
            first_name = "James",
            last_name = "Mwai",
            gender = "male",
            phone_number = "0745890760",
            proffessional="Software Developer",
            subject="Python",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )

            self.python = Course.objects.create(
            name="Python",
            duration_of_course=9,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="backeneddeveloper",
            )

            self.javascript = Course.objects.create(
            name="JavaScript",
            duration_of_course=7,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="fronteddeveloper",
            )

            self.design = Course.objects.create(
            name="Design",
            duration_of_course=5,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="fronteddeveloper",
            )
    def test_teacher_can_teach_a_course(self):
        self.teacher_a.courses.add(self.python)
        self.assertEqual(self.teacher_a.courses.count(),1)
        self.teacher_a.courses.add(self.javascript)
        self.assertEqual(self.teacher_a.courses.count(),2)
        self.teacher_a.courses.add(self.design)
        self.assertEqual(self.teacher_a.courses.count(),3)

    def test_teacher_can_teach_many_courses(self):
        self.teacher_a.courses.add(self.python,self.javascript,self.design)
        self.assertEqual(self.teacher_a.courses.count(),3)