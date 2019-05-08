from django.db import models

# Create your models here.
class HelpType(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a type of help which you need")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Found(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    founder = models.ForeignKey('Found', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="how we can help?")


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('founder-detail', args=[str(self.id)])


import uuid  # Required for unique book instances


class HelpInfo(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for your zapros")
    founder = models.ForeignKey('Found', on_delete=models.SET_NULL, null=True)
    ask = models.CharField(max_length=200)
    answer = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('r', 'Readed'),
        ('f', 'Founding'),
        ('rr', 'Ready'),
        ('p', 'In process'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='r', help_text='We started founding')



    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.founder.title)


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)