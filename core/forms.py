from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "content", "author"]