from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import *

# Create your tests here.
class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Jason', email='jason@ntu.com', password1='abcdefgh', password2='abcdefgh', first_name='Jason', last_name='Tan', is_staff=True)

class User_Form_Test(TestCase):
    def test_form_pass(self):
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password1':'abcdefgh', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertTrue(form.is_valid())

    '''def test_form_pass(self):
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password1':'abcdefgh', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertTrue(form.is_valid())'''

    def test_form_fail_missing_attribute_username(self):
        #missing attribute username
        form=CreateAccountForm(data={'email':'jason@ntu.com', 'password1':'abcdefgh', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_email(self):
        #missing attribute email
        form=CreateAccountForm(data={'username':'Jason', 'password1':'abcdefgh', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertEqual(form.is_valid(), True)

    def test_form_fail_missing_attribute_password1(self):
        #missing attribute password1
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_password2(self):
        #missing attribute password2
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password1':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertEqual(form.is_valid(), False)

    def test_form_fail_missing_attribute_firstname(self):
        #missing attribute firstname
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password1':'abcdefgh', 'password2':'abcdefgh', 'last_name':'Tan', 'is_staff':True})
        self.assertEqual(form.is_valid(), True)

    def test_form_fail_missing_attribute_lastname(self):
        #missing attribute lastname
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com',  'password1':'abcdefgh', 'password2':'abcdefgh', 'first_name':'Jason', 'is_staff':True})
        self.assertEqual(form.is_valid(), True)

    def test_form_fail_missing_attribute_isstaff(self):
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password1':'abcdefgh', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan'})
        self.assertEqual(form.is_valid(), True)

    def test_form_fail_lower_attribute_length_password(self):
        #Attribute length lower than bound for password
        form=CreateAccountForm(data={'username':'Jason', 'email':'jason@ntu.com', 'password1':'abcdefg', 'password2':'abcdefgh', 'first_name':'Jason', 'last_name':'Tan', 'is_staff':True})
        self.assertEqual(form.is_valid(), False)
