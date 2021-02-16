from django.db import models


# Create your models here.
class Orders(models.Model):  
    ID=models.IntegerField(primary_key=True)  
    Order_ID = models.CharField(max_length=30)
    Order_Date = models.CharField(max_length=10)
    Ship_Date = models.CharField(max_length=10)
    Ship_Mode = models.CharField(max_length=100)
    Customer_ID = models.CharField(max_length=30)    
    Customer_Name = models.CharField(max_length=100)
    Segment = models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Postal_Code=models.IntegerField()
    Region=models.CharField(max_length=20)
    Product_ID=models.CharField(max_length=100)
    Category=models.CharField(max_length=1000)
    Sub_category=models.CharField(max_length=1000)
    Product_Name=models.CharField(max_length=2000)
    Sales=models.FloatField()
    Quantity=models.IntegerField()
    Discount=models.FloatField()
    Profit=models.FloatField()
    month=models.CharField(max_length=2)
    Year=models.CharField(max_length=4)