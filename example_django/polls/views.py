from django.shortcuts import render
from .models import Question

from rest_framework import viewsets
from .serializer import QuestionSerializer


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'index.html',context)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer