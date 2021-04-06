import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_check_and_alert(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 40) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', -10) == 'TOO_LOW')
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 4) == 'NORMAL')
        
if __name__ == '__main__':
  unittest.main()
