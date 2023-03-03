from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=30)
    menu = models.ManyToManyField("Link")
    page = models.ForeignKey("Page", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class Link(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ссылка"
        verbose_name_plural = "ссылки"


class Page(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "страница"
        verbose_name_plural = "страницы"
