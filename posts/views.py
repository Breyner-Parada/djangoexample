from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def post_detail(request, post_id):
    return HttpResponse(f"You're looking at post {post_id}")