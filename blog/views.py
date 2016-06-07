from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':post_list})

def detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    post_detail.view += 1
    post_detail.save()
    return render(request, 'blog/detail.html', {'post_detail':post_detail})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '글이 생성됐습니다.')
            return redirect(reverse('blog:detail', args=[post.pk]))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})