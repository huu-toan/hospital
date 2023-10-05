from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
 
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'email', 'phone_number', 'citizen_id', 'medical_record', 'disease_type', 'status']
    
    address = forms.ChoiceField(choices=[
        ('ha-noi', 'Hà Nội'),
        ('da-nang', 'Đà Nẵng'),
        ('nha-trang', 'Nha Trang'),
        ('hai-phong', 'Hải Phòng'),
        ('ha-long', 'Hạ Long'),
        ('phu-quoc', 'Phú Quốc'),
        ('ho-chi-minh', 'Hồ Chí Minh')
    ])
    
    needs = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
