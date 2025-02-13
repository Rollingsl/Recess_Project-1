from .models import FacilityFeedback
from .models import InstructorFeedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import InstructorFeedback, Course


class SignUpForm(UserCreationForm):

    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    










class InstructorForm(forms.ModelForm):
    class Meta:
        model = InstructorFeedback
        fields = ['instructorName', 'department', 'courseUnit', 'knowledge', 'communication', 'teachingStyle',
                  'responsiveness', 'additional_comments']


        widgets = {
            'instructorName': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'courseUnit': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'knowledge': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'communication': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'teachingStyle': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'responsiveness': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'additional_comments': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }


from .models import StudentDetails

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['name', 'studentId', 'emailAddress', 'year_of_study']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'studentId': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'emailAddress': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'year_of_study': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }



class FacilityForm(forms.Form):
    # Choices for Facility Accessibility dropdown
    FACILITY_ACCESSIBILITY_CHOICES = [
        ('fully', 'Fully accessible'),
        ('partial', 'Partially accessible'),
        ('not', 'Not accessible'),
    ]

    # Choices for Rating fields
    RATING_CHOICES = [
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ]

    # Facility name field with a maximum length of 100 characters
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Facility name', 'required': True}),
    )

    # College of facility field with a maximum length of 100 characters
    facility_college = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'College of facility', 'required': True}),
    )

    # Facility accessibility field as a dropdown with predefined choices
    facility_accessibility = forms.ChoiceField(
        choices=FACILITY_ACCESSIBILITY_CHOICES,
        widget=forms.Select(attrs={'required': True}),
    )

    # Rating field for Cleanliness
    cleanliness = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(),
    )

    # Rating field for Maintenance
    maintenance = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(),
    )

    # Rating field for Safety and Security
    safety = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(),
    )

    # Rating field for Resource Availability
    resource_availability = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(),
    )

    # Rating field for Overall facility rating
    facility_rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(),
    )

    # Comment field with a textarea widget for additional comments or suggestions
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Please provide any additional comments or suggestions about our college facilities.', 'rows': 5}
        ),
    )







class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseName', 'courseCode', 'courseDescription', 'effectiveness', 'interest', 'improvement']
        widgets = {
            'courseName': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'courseCode': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'courseDescription': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'effectiveness': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'interest': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'improvement': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }

