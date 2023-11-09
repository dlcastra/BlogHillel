from django import forms

from bloghillel.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 100:
            raise forms.ValidationError("Name is too long, max length is 100")
        return title
