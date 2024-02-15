from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view



# Create your views here.

@api_view(['GET'])
def get_notes(request):
        try:
            note = Notes.objects.filter(username__username = request.user)
            if request.user != note[0].username:
                return Response({
                'status' : 400,
                'message' : 'not athorized user'
                })   
                
            serializer = NotesSerializer(note, many = True)                              
            print(request.user)                    
            return Response(serializer.data)      
            
            
        except Exception as e:
            print(e)
            print(request.user)
            return Response({
                'status' : 500,
                'message' : 'something went wrong'
            })      

class NotesApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]    
    def get(self, request):
        try:
            note = Notes.objects.filter(username = request.user)
            if request.GET.get('search'):
                search = request.GET.get('search')
                note = note.filter(title__icontains = search)
            
            print(request.user)
            serializer = NotesSerializer(note, many = True) 
                                
            return Response(serializer.data)      
            
        except Exception as e:
            print(e)
            print(request.user)
            return Response({
                'status' : 500,
                'message' : 'something went wrong'
            })  
            

    def post(self, request):
        try:
            data = request.data              
            serializer = NotesSerializer(data = data)
            if serializer.is_valid():
                serializer.validated_data['username'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)    
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, id):
        try:
            data = request.data
            obj = Notes.objects.filter(id = id)
            if not obj.exists():
                return Response({
                    'status' : 404,
                    'message' : 'invalid id',
                })
            if request.user != obj[0].username:
              return Response({
                  'status' : 404,
                  'message' : "Not athorized user",     
              })  
            serializer = NotesSerializer(obj[0], data = data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)   
            
            return Response({
                'status' : 404,
                'message' : 'Bad request'
                })      
              
        except Exception as e:
            print(e)
            return Response({
                'status' : 500,
                'data' : {}
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)     
            
    def delete(self, request, id):
        try:
            data = request.data
            obj = Notes.objects.filter(id = id)
            if not obj.exists():
                return Response({
                    'status' : 404,
                    'message' : 'Invalid id',
                })
            if request.user != obj[0].username:
              return Response({
                  'status' : 404,
                  'message' : "Not athorized user",     
              })  
            
            obj[0].delete()
            return Response({
                'status' : 200,
                'message' : 'successfully deleted'
            })  
                 
        except Exception as e:
            print(e)
            return Response({
                'status' : 500,
                'data' : {}
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)         
        
        
        
            
        
            
                         