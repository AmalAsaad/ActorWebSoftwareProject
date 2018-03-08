from django.contrib import admin
# Register your models here.
from .models import Actor,Movie,Prize,UserProfile,Review,Message
admin.site.register(UserProfile)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Prize)
admin.site.register(Review)
admin.site.register(Message)
