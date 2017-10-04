from django.test import TestCase

from user.models import HealthProfessional, User
from user.forms import HealthProfessionalForm


class TestHealthProfessionalForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a'
        self.name_invalid_MAX = 'aasdkgasghdhjadjasvdashdjavcdbnmhasdvbdmmasbdnmhamsjdhgegdhjgsavdhabvdbnasd'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_MIN = '10/12/2010'

        self.phone_valid = '123456789'
        self.phone_invalid = '456'

        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_MAX = 'admin@fgdhafdgfashgdfaghfdasfdghashjasghjasgdhjgasdjasjdjaasdsdfjh.com'
        self.email_invalid_BASE = 'admin@hotmail.com'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.crm_valid = '12345'
        self.crm_valid_existent = '54321'
        self.crm_invalid = '1'
        self.crm_invalid_format = ''

        self.crm_state_valid = 'DF'
        self.crm_state_invalid = 'a'
        self.crm_state_invalid_MAX = 'aaaaaaaa'

        self.id_document_valid = '12345678910'
        self.id_document_invalid = '1234'

        self.password_valid = '1234567'
        self.password_invalid = '1234567891011'
        self.password_invalid_MIN = '123'

        user = HealthProfessional()
        user.crm = "54321"
        user.save()

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_forms_health_professional_is_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms_health_professional_name_is_not_valid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_phone_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_email_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_email_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_MAX,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_email_is_not_valid_BASE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_BASE,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_forms_health_professional_password_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_password_confirmation_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_password_confirmation_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MIN,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_forms_health_professional_crm_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_crm_is_not_valid_existent(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid_existent,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_crm_state_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_invalid_MAX,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}

        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_date_of_birth_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_forms_health_professional_invalid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_invalid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_invalid,
                     'crm_state': self.crm_state_invalid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid1(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid2(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid3(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid4(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid5(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid6(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid7(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid8(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())