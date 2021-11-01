from django.contrib import admin
from . import models

myModels = [models.Account, models.Admin, models.Textbook, models.Seller, models.Buyer, models.Chat_With,
            models.Course, models.University, models.Meet_Up_Info, models.Schedule, models.Complaint, models.Review,
            models.Set_Cost, models.TC]
admin.site.register(myModels)

# Register your models here.
