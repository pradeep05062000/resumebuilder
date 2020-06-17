from django import forms


class ResumeForm(forms.Form):
    name=forms.CharField()
    number=forms.IntegerField(label="Mobile No.")
    address=forms.CharField()
    email=forms.EmailField()
    education=forms.CharField(widget=forms.Textarea)
    skills=forms.CharField(widget=forms.Textarea)
    project=forms.CharField(widget=forms.Textarea)
    pdetails=forms.CharField(label="Personal Details",widget=forms.Textarea)
    declaration=forms.CharField(widget=forms.Textarea)
