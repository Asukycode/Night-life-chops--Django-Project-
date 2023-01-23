from django.db import models



class Meal(models.Model):
          name = models.CharField(max_length=200)
          image = models.ImageField(upload_to = "static/media/")
          calories_number = models.CharField(max_length=3, default="45", null=True, blank=True)
          protein_number = models.CharField(max_length=3, default="50.6", null=True, blank=True)
          price = models.DecimalField(decimal_places=2, max_digits=10)
          rating = models.DecimalField(decimal_places=2, max_digits=3)
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)


          def __str__(self):
                    return self.name

          def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
                    return reverse("products:detail", kwargs={"id": self.id})


