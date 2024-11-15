from django import forms
from student_app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'admission_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Admission Number'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Gender'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control','accept': 'image/*','tittle':'Upload image here'})
        }