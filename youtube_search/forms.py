from django import forms


class YoutubeForm(forms.Form):
    q = forms.CharField(label='q',  max_length=50)
    maxResults = forms.IntegerField(min_value=1, max_value=20, initial=1)
    location = forms.CharField(max_length=36, required=False,
                               widget=forms.TextInput(attrs={'placeholder': '49.62204323535563, 34.5206964068785'}))
    location_radius = forms.IntegerField(max_value=1000, label='Radius, (km)', required=False)
    publishedAfter = forms.DateTimeField(label='Published after:', required=False)
    publishedBefore = forms.DateTimeField(label='Published before:', required=False)

    def __init__(self, *args, **kwargs):
        super(YoutubeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
