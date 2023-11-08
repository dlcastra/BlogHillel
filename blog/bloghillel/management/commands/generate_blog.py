import random

from django.core.management.base import BaseCommand
from faker import Faker
from bloghillel.models import Blog

fake = Faker()


class Command(BaseCommand):
    help = (
        "Fills the database with fake blog posts"
        "\n\n\tTo fill the table with data, specify the number of titles"
        "\nThe base value of titles is 10"
    )

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, nargs="?", default=10)

    @staticmethod
    def generate_content():
        text = ""
        for _ in range(random.randrange(15, 30)):
            text += fake.text() + " "

        return text

    def handle(self, *args, **options):
        number = options["number"]
        if number < 1:
            self.stdout.write(
                self.style.ERROR("The number to be generated must be greater than 0")
            )
        else:
            for i in range(number):
                blog_content = self.generate_content()
                blog = Blog(
                    title=fake.sentence(),
                    content=blog_content,
                    updated_at=fake.date_time_this_decade(tzinfo=None),
                )

                blog.save()

            self.stdout.write(self.style.SUCCESS("The blog was successfully generated"))
