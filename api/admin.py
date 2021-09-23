from django.contrib import admin
from .models import Playlist
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Playlist)

class PlaylistAdmin(ImportExportModelAdmin):
    list_display = ['id','title','danceability','energy','key','loudness','mode','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signture','num_bars','num_sections','num_segments','classes','star_rating']
    pass
