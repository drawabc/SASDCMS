from django.test import TestCase
from CMSApp.views import *
from authentication import *

# Create your tests here.

class ReportFireTestCase(TestCase):
    def setUp(self):
        Report.objects.create(name="Justin", mobile="85007341", location="850 Jurong West Street 81", unit_number="#02-02", postal_code="640850", description="Fire broke out at my kitchen", type="EA")

    def tearDown(self):
        c=Report.objects.get(name="Justin")
        c.delete()

    def test_correct_data_submission(self):
        crisis=Report.objects.get(name="Justin")
        self.assertEqual(crisis.postal_code, "640850")
