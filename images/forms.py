from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = self._get_extension_from_url(url)
        if extension not in valid_extensions:
            raise forms.ValidationError("The given URL doesn't match valid image extensions. Only jpg, jpeg and png")
        return url

    def save(self, user, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)

        image_url = self.cleaned_data['url']
        image_name = "{}.{}".format(slugify(image.title), self._get_extension_from_url(image_url))

        #download image
        response = request.urlopen(image_url)

        image.user = user
        image.image.save(image_name, ContentFile(response.read()))

        image.save()

        return image

    def _get_extension_from_url(self, url):
        return url.rsplit('.', 1)[1].lower()
