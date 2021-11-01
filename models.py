from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    blocked = models.BooleanField(default=False)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.username


class Admin(models.Model):
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    privileges = models.TextField(default=None, blank=True)
    tasks = models.TextField(default=None, blank=True)
    responsibilities = models.TextField(default=None, blank=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.username)


class Buyer(models.Model):
    username = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True)
    username = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.username)


class Seller(models.Model):
    username = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.username)


# use the auto <int:pk>
class Chat_With(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    exchange_method = models.CharField(max_length=10)
    negotiated_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return 'Buyer:%s, Seller:%s' % (self.buyer_id, self.seller_id)


class Textbook(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    condition = models.CharField(max_length=50)
    publisher = models.CharField(max_length=255)
    additional_details = models.TextField(blank=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.id


# use the auto <int:pk>
class Review(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        app_label = 'api'

    def __str__(self):
        return 'Buyer:%s, Seller:%s' % (self.buyer_id, self.seller_id)


# use the auto <int:pk>
class Complaint(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    details = models.TextField(default="")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.buyer)


# use the auto <int:pk>
# might have to re-think implementation of this relation?
class Schedule(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    listEvents = models.TextField()

    class Meta:
        app_label = 'api'

    def __str__(self):
        return 'Buyer:%s, Seller:%s' % (self.buyer_id, self.seller_id)


# use the auto <int:pk> ? Should refer to buyer_id but that alone isn't unique
# re-think how to implement this relation
class Meet_Up_Info(models.Model):
    username = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    type = models.CharField(max_length=50)
    additionalCharge = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.username)


class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    university = models.ForeignKey('University', on_delete=models.CASCADE)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.course_id


class University(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    city = models.CharField(max_length=50)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.name

# use the auto <int:pk>
class Set_Cost(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    textbook_id = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    asking_price = models.DecimalField(max_digits=5, decimal_places=2)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    negotiable = models.BooleanField(default=False)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return f"Textbook:{self.textbook_id}, Seller:{self.seller_id}"

class TC(models.Model):
    textbook_id = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return f"Textbook:{self.textbook_id}, Course:{self.course_id}"
