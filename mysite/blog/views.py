from django.shortcuts import render, get_object_or_404 
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_home(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts en cada página
    page = request.GET.get('page')
    try:
      posts = paginator.page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = paginator.page(paginator.num_pages)

    post_featured1 = Post.feature.all()[0]
    post_featured2 = Post.feature.all()[1]
   # post_featured3 = Post.feature.all()[2]
   # post_featured4 = Post.feature.all()[3]
   # post_featured5 = Post.feature.all()[4]

    promoted_posts = Post.promote.all()
    post_promoted1 = Post.promote.all()[0]
    post_promoted2 = Post.promote.all()[1]
   # post_featured3 = Post.feature.all()[2]
   # post_featured4 = Post.feature.all()[3]
   # post_featured5 = Post.feature.all()[4]

    context = {
        'posts': posts,
        'promoted_posts': promoted_posts,
        'post_featured1': post_featured1,
        'post_featured2': post_featured2,
      #  'post_featured3': post_featured3,
      #  'post_featured4': post_featured4,
      #  'post_featured5': post_featured5,
        'post_promoted1': post_promoted1,
        'post_promoted2': post_promoted2,
      #  'post_featured3': post_featured3,
      #  'post_featured4': post_featured4,
      #  'post_featured5': post_featured5
    }
    return render(request,
                  'blog/post/list.html',
                  context)


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list_00.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})