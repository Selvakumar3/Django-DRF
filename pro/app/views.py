from rest_framework import serializers
from rest_framework import status
from .models import Books
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView

###############################################################################
   # function based views
   
   
@api_view(['POST'])

def add (request):
    item = BooksSerializer(data= request.data)
    if item.objects.filter(**request.data).exist():
        raise serializers.ValidationError(" the data already exists ")
    
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])

def view(request):
    
    
    if request.query_params:
        items = Books.objects.filter(**request.query_param.dict())
    else:
        items = Books.objects.all()
  
 
    if items:
        data = BooksSerializer(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(['POST'])

def update(request, pk):
    item = Books.objects.get(pk=pk)
    data = BooksSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)      
    
    
@api_view(['DELETE'])

def delete(request, pk):
    item = get_object_or_404(Books, pk=pk)
    item = Books.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)    

##########################################################################################################

@api_view (['GET'])

def booklist(request):
    books = Books.objects.all()
    serializers = BooksSerializer(books, many = True)
    return Response(serializers.data)

@api_view (['GET'])

def bookdetails(request,pk):
    books = Books.objects.get(id=pk)
    serializers = BooksSerializer(books, many = False)
    return Response(serializers.data)

@api_view (['POST'])

def bookcreate(request):
    serializers = BooksSerializer(data=request.data)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    
   
@api_view (['POST'])  
   
def bookupdate(request, pk):
    book = Books.objects.get(id=pk)
    serializers = BooksSerializer(instance=Books, data=request.data)
    
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)  

@api_view(['DELETE'])

def bookdelete(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()
    
    return Response('Deleted')
  
###############################################################################
                        # class based views 

class BooksList(APIView):
   
    def get(self, request, format=None):
        book = Books.objects.all()
        serializer = BooksSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BooksDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BooksSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BooksSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
    #####################################################################
   # generics based views
   
class StudentsList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class Studentsdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer