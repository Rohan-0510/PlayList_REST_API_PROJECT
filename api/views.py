from django.shortcuts import render,Http404
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView 

class playlist_list(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

@api_view(['GET','PUT'])
def playlist_option(request,name=None):
	if request.method == "GET":
        	if name is None:
            		result = Playlist.objects.all()
            		sresult = PlaylistSerializer(result,many=True)
            		return Response(sresult.data)
        	else:
            		try:
                		result = Playlist.objects.get(title = name)
                		sresult = PlaylistSerializer(result)
                		return Response(sresult.data) 
            		except Playlist.DoesNotExist:
                		raise Http404

	elif request.method == "PUT":
		play = Playlist.objects.get(title=name)
		serializer = PlaylistSerializer(play,data = request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Playlist Upadated'})
		else:
			return Response(serializer.errors)

	
	