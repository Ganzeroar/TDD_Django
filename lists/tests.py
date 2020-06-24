from django.test import TestCase

class SmokeTest(TestCase):
    '''stupid test'''

    def test_bad_math(self):
        '''dont using test'''
        self.assertEqual(1+1, 3)