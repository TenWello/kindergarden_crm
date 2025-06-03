from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', null=True, blank=True)  # upload_to ni soddaroq yozdim
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'self',  # self-referential, ya’ni Category ichida Category
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'  # Kategoriyaning bolalari
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        # Cheksiz rekursiyani oldini olamiz
        names = [self.name]
        parent = self.parent
        max_depth = 10
        while parent and max_depth > 0:
            if parent == self:
                break  # O'zini parent qilib yuborilgan bo'lsa cheksiz sikl bo'lmaydi
            names.append(parent.name)
            parent = parent.parent
            max_depth -= 1
        return " / ".join(reversed(names))


