import unittest
from Agape_Family22 import*

root = Tk()
sms = ankit(root)
class final(unittest.TestCase):
    def test_searching(self):
        sms.Search_With.set('ID')

        list = [(1, 'Ankit', 'Shankar', 'BSC(Hons) in Ethical Hacking', 'Damak', 20, '9861839797', 'Male'),
                (2, 'Anju', 'Shrestha', 'BSC(Hons) in Ethical Hacking', 'Kapan', 19, '9818987267826', 'Female')]
        ex_result = [(1, 'Ankit', 'Shankar', 'BSC(Hons) in Ethical Hacking', 'Damak', 20, '9861839797', 'Male')]

        ac_result = sms.search_algo(list, '1')
        self.assertEqual(ac_result, ex_result)

    def test_sorting(self):

        array_test = [(1, 'Ankit', 'Shankar', 'BSC(Hons) in Ethical Hacking', 'Damak', 20, '9861839797', 'Male'),
                (2, 'Anju', 'Shrestha', 'BSC(Hons) in Ethical Hacking', 'Kapan', 19, '9818987267826', 'Female')]
        exp_result = [(2, 'Anju', 'Shrestha', 'BSC(Hons) in Ethical Hacking', 'Kapan', 19, '9818987267826', 'Female'),(1, 'Ankit', 'Shankar', 'BSC(Hons) in Ethical Hacking', 'Damak', 20, '9861839797', 'Male')]

        ac = sms.insertion_sort(array_test, 'Descending')
        self.assertEqual(ac, exp_result)



if __name__=='__main__':

    unittest.main()