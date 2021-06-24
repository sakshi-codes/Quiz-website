from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question,Answer
from results.models import Result
# Create your views here.

#Creates the list of quizes(link)
class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'
#After creating the quiz through django admin 
def quiz_view(request,pk):
    quiz = Quiz.objects.get(pk=pk) #sets the primary key 
    return render(request,'quizes/quiz.html',{'obj':quiz}) # assigns the value to obj and renders the template quizes/quiz.html and 

def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = [] #empty question list
    for q in quiz.get_questions(): 
        answers = [] #empty answers list
        for a in q.get_answers():
            answers.append(a.text) # first appending answers of questions in list answers
        questions.append({str(q): answers}) # then creating list questions with answers(dictionary) key=question and assigning list of answers
    return JsonResponse({
        'data': questions,  
        'time': quiz.time,
    })
def save_quiz_view(request,pk):
    if request.is_ajax():
        questions =[] #empty question list
        data = request.POST
        data_ = dict(data.lists()) #converting query to dict to simple dict 
        del data_['csrfmiddlewaretoken']
        print(data_)
        for k in data_.keys(): #keys are questions 
              question = Question.objects.get(text=k) # getting questions with keys
              questions.append(question) #appending questions in questions list
        print(questions)

        user = request.user #getting user
        quiz = Quiz.objects.get(pk=pk) #getting quiz by pirmary key
        #result part
        score = 0 #intially 0
        multiplier = 100/quiz.number_of_questions #maximum score is 100 so score per question is 100/no.of questions
        results = []
        correct_answer = None
        
        for q in questions:
            a_selected = request.POST.get(q.text) #Getting answer selected
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q) #getting answer of question
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q) : {'correct_answer':correct_answer,'answered': a_selected}})
            else:
                results.append({str(q) : 'not answered'})
        score_ = score * multiplier
        Result.objects.create(quiz = quiz , user=user,score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed' : True,'score':score_,'results':results})
        elif score_ < quiz.required_score_to_pass:
            return JsonResponse({'passed' : False, 'score':score_ , 'results':results})
