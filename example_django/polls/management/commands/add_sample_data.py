from typing import Any
from django.core.management.base import BaseCommand
from polls.models import Question
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Add sample date to the polls app'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        question = [
            "What's new?",
            "What's up?",
            "How are you?",
            "What's your favorite color?",
            "What's your favorite food?"
        ]

        for i, question_text in enumerate(question):
            pub_date = timezone.now() - datetime.timedelta(days=i)
            Question.objects.create(question_text=question_text,pub_date=pub_date)

        self.stdout.write(self.style.SUCCESS('Successfully added sample data'))