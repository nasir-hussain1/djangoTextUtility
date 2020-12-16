from django.http import HttpResponse
from django.shortcuts import render


def index(request):    
    return render(request, 'index.html')


# def removePunctuation(request):
#     text = request.GET.get('inputText', 'default')
#     print(text)
#     return HttpResponse('''<h1>Remove Punctuation</h1><a href="/">Go to home </a> ''')


# def capitalizeFirst(request):
#     return HttpResponse('''<h1>Capitalize First Letter</h1><a href="/">Go to home </a> ''')


# def removeNewLine(request):
#     return HttpResponse('''<h1>Remove New Line</h1><a href="/">Go to home </a> ''')


# def removeSpace(request):
#     return HttpResponse('''<h1>Remove Space</h1><a href="/">Go to home </a> ''')


# def charactersCount(request):
#     return HttpResponse('''<h1>Count the characters</h1><a href="/">Go to home </a> ''')

def analyze(request):

    text = request.POST.get('inputText', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remnewline = request.POST.get('remnewline', 'off')
    charcount = request.POST.get('charcount', 'off')
    remspace = request.POST.get('remspace', 'off')

    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''    
    
    analyzedText = '' 
    purpose =''
    params={}

    if ((remspace == 'off') and (charcount == 'off')and (remnewline == 'off' ) and(capitalize=='off') and(removepunc == 'off')):
        print(text)
        error={'error': 'Please select an option'}
        return render(request, 'error.html', error)
        
    else:
        

        if (removepunc != 'off'):
            for char in text:
                if char not in punc:
                    analyzedText =analyzedText+char
            text = analyzedText
            
            purpose +='Puncuation is removed,'
            params = {'purpose':purpose,'analyzedText':analyzedText}
            analyzedText = ''
            #return render(request, 'analyze.html', params )
        
        if (capitalize !='off'):
            
            for char in text:
                analyzedText += char.upper()
            text = analyzedText
            purpose +='All text is capitalized,'
            params = {'purpose':purpose,'analyzedText':analyzedText}
            analyzedText = ''
            #return render(request,'analyze.html',params)
        
        if (remnewline != 'off'):
            for char in text:
                if ((char != "\n") and (char!= "\r")):
                    analyzedText +=char
            text = analyzedText
            purpose +='Newlines are removed,'
            params = {'purpose':purpose,'analyzedText':analyzedText}
            analyzedText = ''
            
            #return render(request, 'analyze.html', params )
        
        
            
        
        if (remspace != 'off'):
            for index, char in enumerate(text):
                if not(text[index] == " " and text[index+1]==" "):
                    analyzedText +=char
            text = analyzedText
            purpose +='Extra spacing is removed,'
            params = {'purpose':purpose,'analyzedText':analyzedText}
            analyzedText = ''
        
        if (charcount != 'off'):
            totalchar = str(len(text))
            
            #analyzedText =totalchar
            #text = analyzedText
            purpose +='Total characters are counted,'
            params = {'purpose':purpose, 'totalchar':totalchar, 'analyzedText':text}
            print(analyzedText)
    return render(request, 'analyze.html', params)

    
    
    