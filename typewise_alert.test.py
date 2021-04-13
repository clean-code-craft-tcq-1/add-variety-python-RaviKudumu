import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_check_and_alert_passive_cooling(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 40) == 'TOO_HIGH')

    def test_check_and_alert_hi_active_cooling(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONSOLE', 'HI_ACTIVE_COOLING', -10) == 'TOO_LOW')
    def test_check_and_alert_med_active_cooling(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 4) == 'NORMAL')
    def test_send_status_to_controller(self):
        self.assertTrue(typewise_alert.send_status_to_controller('TOO_HIGH') == 'TOO_HIGH')
    def test_send_status_to_console(self):
        self.assertTrue(typewise_alert.send_status_to_console('TOO_LOW') == 'TOO_LOW')
    def test_send_status_email(self):
        self.assertTrue(typewise_alert.send_status_email('NORMAL') == 'NORMAL')

if __name__ == '__main__':
  unittest.main()
