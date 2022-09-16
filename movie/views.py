from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from movie.models import Movie
from movie.serializers import MovieSerializer


class GetMovieAV(generics.ListAPIView):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args , *kwargs)


class CreateMovieAV(generics.CreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAdminUser]

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


class MovieDetailAV(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args , *kwargs)


class UpdateAV(generics.UpdateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args , *kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args , *kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)