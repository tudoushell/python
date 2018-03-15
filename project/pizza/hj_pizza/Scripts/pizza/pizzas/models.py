from django.db import models

class Pizza(models.Model):
    pizza_name=models.CharField(max_length=40)
    # text=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='pizza'
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE,)
    # name=models.CharField(max_length=50)
    name=models.TextField()
    date_added=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural='pizza_stuff'
    
    def __str__(self):
        return self.name[:5]+'...'
