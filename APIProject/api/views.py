from django.shortcuts import render,HttpResponse
from .models import Article,Images
from .serializers import ArticleSerializer,UserSerializer,ImageSerializer
from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class=ImageSerializer
    def get_queryset(self):
        user=self.request.user
        return Images.objects.filter(user=user)
    permission_classes=[IsAuthenticated]
    authentication_classes = (TokenAuthentication,)        

class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class=UserSerializer








'''
class ArticleList(generics.GenericAPIView,mixins.ListModelMixin,
                mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class ArticleDetails(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='id'
    def get(self,request,id):
        return self.retrieve(request,id=id)
    def put(self,request,id):
        return  self.update(request,id=id)
    def delete(self,request,id):
        return self.destroy(request,id=id)      

      
   '''
'''
class ArticleList(APIView):

    def get(self,request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    '''



# Create your views here.
'''
@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_details(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    '''

    
  