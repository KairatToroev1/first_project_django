from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from tags.models import Tag
from tags.forms import TagForm


def tags_list_view(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tags_list.html', context={'tags': tags})


def tag_detail_view(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'tags/tag_detail.html', context={'tag': tag})


class TagCreateView(View):

    def get(self, request):
        form = TagForm()
        return render(request, 'tags/tag_create.html', context={'form': form})

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            return redirect(tag)
        return render(request, 'tags/tag_create.html', context={'form': form})


class TagUpdateView(View):

    def get(self, request, id):
        post = get_object_or_404(Tag, id=id)
        bound_form = TagForm(instance=post)
        return render(request, 'tags/tag_update.html', context={'form': bound_form,
                                                                  'post': post})

    def post(self, request, id):
        post = get_object_or_404(Tag, id=id)
        form = TagForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
        return render(request, 'tags/tag_update.html', context={'form': form, 'post': post})


class TagDeleteView(View):

    def get(self, request, id):
        post = get_object_or_404(Tag, id=id)
        return render(request, 'tags/tag_delete.html', context={'post': post})

    def post(self, request, id):
        post = get_object_or_404(Tag, id=id)
        post.delete()
        return redirect(reverse('tags_list_url'))
