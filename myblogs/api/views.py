from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/blogs/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of blogs'
        },
        {
            'Endpoint': '/blogs/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single blog object'    
        },
        {
            'Endpoint': '/blogs/create/',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'Creates new blog with data sent in post request'  
        },
        {
            'Endpoint': '/blogs/id/update/',
            'method': 'PUT',
            'body': {'body': ''},
            'description': 'Updates an existing node with data sent in post request'
        },
        {
            'Endpoint': '/blogs/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing blog'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getBlogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createBlog(request):
    data = request.data
    blog = Blog.objects.create(
        title=data["title"],
        author=data["author"],
        body=data["body"]
    )
    serializer = BlogSerializer(instance=blog, data=data)
    return Response(serializer.data)

@api_view(['PUT'])
def updateBlog(request, pk):
    data = request.data
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    print(blog)
    blog.delete()
    return Response('Note was deleted!')

