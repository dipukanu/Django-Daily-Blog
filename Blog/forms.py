from .models import contact, blog
from django import forms

class contact_frm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

        labels={
            'name':'Name: ', 'email':'Email: ', 'comments':'Message: '
        }

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter your email'}),
            'comments':forms.Textarea(attrs={'placeholder':'Write your message'}),
        }

class blog_frm(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'

        labels={
            'blog_heading':'Blog Title: ', 'blog_image':'Blog Image: ', 'blog_desc':'Blog Description: ', 'pub_name':'Published By: '
        }

        widgets={
            'blog_heading':forms.TextInput(attrs={'placeholder':'Enter your blog title'}),
            'blog_desc':forms.Textarea(attrs={'placeholder':'Write something about your blog'}),
            'pub_name':forms.TextInput(attrs={'placeholder':'Write the publisher name'}),
        }



