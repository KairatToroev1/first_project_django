from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from posts.models import Post
from posts.forms import PostForm, SearchForm
from comments.forms import CommentForm

def post_detail_view(request,id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments
            , 'comment_form': comment_form, 'new_comment': new_comment})

    else:
        comment_form = CommentForm()
        return render(request,'posts/post_detail.html', {'post': post,'comments': comments
                                                     , 'comment_form': comment_form})


def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/index.html', context={'posts': posts})
    elif request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_param = search_form.cleaned_data.get('search_param')
            filtered_posts = Post.objects.filter(title__icontains=search_param)
            return render(request,'posts/index.html',context={'posts': filtered_posts})




class PostCreateView(View):

    def get(self, request):
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
        return render(request, 'posts/post_create.html', context={'form': form})


class PostUpdateView(View):

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        bound_form = PostForm(instance=post)
        return render(request, 'posts/post_update.html', context={'form': bound_form, 
                                                                  'post': post})

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
        return render(request, 'posts/post_update.html', context={'form': form, 'post': post})


class PostDeleteView(View):

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        return render(request, 'posts/post_delete.html', context={'post': post})

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect(reverse('posts_list_url'))
