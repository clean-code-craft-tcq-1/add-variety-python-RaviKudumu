import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_check_and_alert_passive_cooling(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 40)[0] == 'TOO_HIGH')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 40)[1] == 'Controller')

    def test_check_and_alert_hi_active_cooling(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONSOLE', 'HI_ACTIVE_COOLING', -10)[0] == 'TOO_LOW')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONSOLE', 'HI_ACTIVE_COOLING', -10)[1] == 'Console')

    def test_check_and_alert_med_active_cooling(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 4)[0] == 'NORMAL')
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 4)[1] == 'Email')
if __name__ == '__main__':
  unittest.main()
