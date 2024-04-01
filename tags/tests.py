from django.test import TestCase
from .models import Tag
# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="tag1")
        Tag.objects.create(name="tag2")
          

    def test_get_tags(self):
        
        tags = Tag.objects.all()
        self.assertEqual(tags.count(), 2)
        self.assertEqual(tags[0].name, 'tag1')
        self.assertEqual(tags[1].name, 'tag2')

        #check auto generated fields
        self.assertIsNotNone(tags[0].created_at)
        self.assertIsNotNone(tags[0].updated_at)
        self.assertIsNotNone(tags[0].id)
        self.assertIsNotNone(tags[1].created_at)
        self.assertIsNotNone(tags[1].updated_at)
        self.assertIsNotNone(tags[1].id)
    
    def test_delete_tag(self):
        tag = Tag.objects.get(name="tag1")
        tag.delete()
        tags = Tag.objects.all()
        self.assertEqual(tags.count(), 1)
        self.assertEqual(tags[0].name, 'tag2')



        
        