from django import forms
from recipeapp.models import Login,Recipe

# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model=Recipe
#         fields='__all__'
#
class RegisterForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        widgets={'password':forms.PasswordInput,
                 'repassword':forms.PasswordInput
                 }