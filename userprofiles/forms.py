from django.forms import ModelForm
from userprofiles.models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder, Tab

class UserProfileForm(ModelForm):
    helper = FormHelper()
    helper.form_tag = True
    helper.form_method = "POST"
    helper.form_action = "/accounts/edit_profile/"
    helper.add_input(Submit('submit', 'Submit'))
    helper.layout = Layout(
	TabHolder(
       Tab(
		'Basic Information',
		'first_name',
		'last_name',
		'phone_number',
		'ssn',
      ),
        Tab(
		'Address',
		'address1',
		'address2',
		'city',
		'state',
		'zip_code',
        )
	)
)

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'ssn', 'address1', 'address2', 'city', 'state', 'zip_code',)
        exclude = ('user',)
