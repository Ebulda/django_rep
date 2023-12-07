from django import forms

from post.models import Category, Review


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="------", required=False,
                                      initial=None)

    def clean_content(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if len(content) < 30:
            raise forms.ValidationError("Content too short!")
        if not content:
            raise forms.ValidationError("Content is rewired!")
        return cleaned_data


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text']


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {'text': forms.Textarea(), 'product': forms.HiddenInput()}
