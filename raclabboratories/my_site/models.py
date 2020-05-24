from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    impurity_name = models.CharField(max_length=1024,unique=True)
    chemical_name = models.CharField(max_length=512)
    cas_no = models.CharField(max_length=128)
    quantity = models.DecimalField(decimal_places=2,max_digits=10)
    current_price = models.DecimalField(decimal_places=2,max_digits=10)
    actual_price = models.DecimalField(decimal_places=2,max_digits=10)
    image_file = models.ImageField(upload_to="impurities")

    def __str__(self):
        return self.impurity_name

    def get_absolute_url(self):
        return reverse("my_site:post_list")

class PostDetails(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_details")
    solubility = models.CharField(max_length=256)
    expiry_date = models.DateField()
    purity = models.DecimalField(decimal_places=2,max_digits=4)
    place = models.CharField(max_length=512)
    state = models.CharField(max_length=333,blank=True)
    mol_wt = models.CharField(max_length=333,blank=True)
    mol_fm = models.CharField(max_length=111,blank=True)
    
    def __str__(self):
        return self.post.impurity_name

class Order(models.Model):
    order = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="orders")
    name = models.CharField(max_length=512)
    mobile = models.CharField(max_length=521,help_text = "Default extension (+91).\nPlease enter the pin-code in case of telephone")
    email = models.EmailField(max_length=256,help_text="We dont spam you..!!")
    place = models.CharField(max_length=512,blank=True)
    description = models.TextField(max_length=11111,blank=True)
    
    def __str__(self):
        return self.name
    

