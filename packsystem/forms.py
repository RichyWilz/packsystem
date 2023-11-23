
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length= 15, help_text= '*' )
    first_name = forms.CharField(max_length = 30, help_text= '*')
    last_name = forms.CharField(max_length = 30, required=False) #help_text= 'Optional')
    email = forms.EmailField(max_length=200) #help_text = 'Enter valid e-mail address')
    course = forms.CharField(max_length= 35, required= True , help_text='*')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'course',
        ]

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control","placeholder":"Enter your username"}),
             'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first name'}),
             'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last name'}),
             'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email address'}),
             'course': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your course'}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your password'}),
             'password1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm your password'}),
         }
        

class AddUserForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=3, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})) 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


# class AddOrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'client', 'receiver', 'delivery_date', 'status']

    # def __init__(self, *args, **kwargs):
    #     super(AddOrderForm, self).__init__(*args, **kwargs)
    #     self.fields['delivery_date'].widget = forms.DateInput(attrs={'type': 'date'})

    # def clean_delivery_date(self):
    #     # Convert the delivery_date to a string before passing it to the JSON encoder
    #     return str(self.cleaned_data['delivery_date'])

# class AddOrderForm(UserCreationForm):
#     username = forms.CharField(required=True, min_length=3, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})) 
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

#     # orderId = models.CharField(max_length=50, unique=True)
#     # name = models.CharField(max_length=100)
#     # client = models.CharField(max_length=100)
#     # receiver = models.CharField(max_length=100)
#     # delivery_date = models.DateField()
#     # status = models.CharField(max_length=20)

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
         
