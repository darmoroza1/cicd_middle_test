from django.test import TestCase, RequestFactory
from django.urls import reverse
from recipe.models import Category, Recipe
from recipe.views import main, category_list
import unittest

class MainViewTest(TestCase):
    def setUp (self):
        self.factory = RequestFactory()

    def test_main_view (self):
        url = reverse('main')
        request = self.factory.get(url)

        # Створення тестових даних
        recipe1 = Recipe.objects.create(name='Recipe 1')
        recipe2 = Recipe.objects.create(name='Recipe 2')
        recipe3 = Recipe.objects.create(name='Recipe 3')

        response = main(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, recipe1.name)
        self.assertContains(response, recipe2.name)
        self.assertContains(response, recipe3.name)


class CategoryListViewTest(TestCase):
    def setUp (self):
        self.factory = RequestFactory()

    def test_category_list_view (self):
        url = reverse('category_list')
        request = self.factory.get(url)

        # Створення тестових даних
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')
        recipe1 = Recipe.objects.create(name='Recipe 1', category=category1)
        recipe2 = Recipe.objects.create(name='Recipe 2', category=category1)
        recipe3 = Recipe.objects.create(name='Recipe 3', category=category2)

        response = category_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertContains(response, category1.name)
        self.assertContains(response, category2.name)
        self.assertContains(response, recipe1.name)
        self.assertContains(response, recipe2.name)
        self.assertContains(response, recipe3.name)


if __name__ == '__main__':
    unittest.main()
