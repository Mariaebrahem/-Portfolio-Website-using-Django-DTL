from django.shortcuts import render

def home(request):
    context = {
        'user': {
            'name': 'maria',
            'bio': 'I am a full-stack developer with a passion for learning and building modern web applications.'
        },
        'skills': ['python','php', 'django', 'html', 'css', 'javascript'],
    }
    return render(request, 'pages/home.html', context)


