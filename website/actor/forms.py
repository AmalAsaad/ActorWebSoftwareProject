from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile,Review



class UserFormRegister(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #age = forms.IntegerField(required=False)
    #country = forms.CharField(max_length=30,required=False)
    #phone = forms.IntegerField(required=False)
   # img = forms.ImageField(required=False)
    class Meta:
        model = User
    #    fields =  ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','age','country','phone','img']
        fields =  ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

   # def __init__(self, *args, **kwargs):
    #    user = kwargs.pop('user', '')
     #   super(UserFormRegister, self).__init__(*args, **kwargs)
      #  self.fields['user_defined_code'] = forms.ModelChoiceField(queryset=User.objects.filter(username=user))

    def save(self, commit=True):
        user = super(UserFormRegister, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        #user.age = self.cleaned_data['age']
     #   user.country = self.cleaned_data['country']
      #  user.phone = self.cleaned_data['phone']
       # user.img= self.cleaned_data['img']
  #      user.bio = self.cleaned_data['bio']
        if commit:
            user.save()

        return user







class UserFormEdit(UserChangeForm):
    # age = forms.IntegerField(required=False)
    # country = forms.CharField(max_length=30, required=False)
    # phone = forms.IntegerField(required=False)
    # img = forms.ImageField(required=False)
    # bio = forms.CharField(max_length=1000, required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    def save(self, commit=True):
        user = super(UserFormEdit, self).save(commit=False)
     #    user.age = self.cleaned_data['age']
     #    user.country = self.cleaned_data['country']
     #    user.phone = self.cleaned_data['phone']
     # #   user.bio = self.cleaned_data['bio']
     #    user.img = self.cleaned_data['img']
        if commit:
            user.save()

        return user





class ReviewForm(forms.Form):
    review_area = forms.CharField(label="",widget=forms.Textarea)


class MessageForm(forms.Form):
    message_area = forms.CharField(label="",widget=forms.Textarea)


class CommentForm(forms.Form):
    parent_comment = forms.IntegerField(widget=forms.HiddenInput,required=False)
    comment_area = forms.CharField(label="",widget=forms.Textarea)
