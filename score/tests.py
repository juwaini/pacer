import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from score.models import Score


class ScoreTest(TestCase):
    def setUp(self) -> None:
        self.u1 = User.objects.create(username='usertest1')
        self.u2 = User.objects.create(username='usertest2')

    def test_correct_score(self):
        Score.objects.create(user=self.u1, score=10, last_check=datetime.datetime.now())
        Score.objects.create(user=self.u2, score=15, last_check=datetime.datetime.now())

        self.assertEqual(Score.objects.all().count(), 2)

    def test_incorrect_score(self):
        Score.objects.create(user=self.u1, score=1.5, last_check=datetime.datetime.now())
        s = Score.objects.get()

        self.assertEqual(s.score, 1.5)
