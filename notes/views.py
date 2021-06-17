#from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render,redirect

from django.template import loader
from django.http import HttpResponse
from .models import AIUser
#from .models import Note
from django.views import generic
#from .forms import NoteForm 
from google.cloud import vision
import os
import logging
import base64

# Create your views here.
class IndexView(generic.ListView):
   #model = Note  
   template_name = 'notes/index.html'
   
   def get_queryset(self):
    notes = Note.objects
    return notes; 


logger = logging.getLogger("ai_recruiter_logger")

def login(request):
    """
    login page call

    Parameters
    ----------
    request : HttpRequest
         request object

    Returns
    -----------
     HttpResponse
        content is the result of render method     
    """

    template_name = 'notes/login.html'
    return render(request, template_name)
def logout(request):
    """
    logout page call

    Parameters
    ----------
    request : HttpRequest
         request object

    Returns
    -----------
     HttpResponse
        content is the result of render method     
    """
    template_name = 'notes/login.html'

    return render(request, template_name)    


def home(request):
   
    context = {}
    return render(request, 'notes/index.html', context) 

def voice(request):
   
    context = {}
    return render(request, 'notes/index.html', context) 

def chatbot(request):
   
    context = {}
    return render(request, 'notes/chatbot.html', context) 

def digital(request):
   
    context = {}
    return render(request, 'notes/digital_assistant.html', context) 



def clinic(request):
   
    context = {}
    return render(request, 'notes/clinic_assistant.html', context) 

def prescription(request):
   
    context = {}
    return render(request, 'notes/upload_prescription.html', context) 

def scanp(request):
     
    image_url = request.POST['prescription']
    #password = request.POST['password']
    """Change your endpoint"""
    # [START vision_set_endpoint]

    #import vision
    client_options = {'api_endpoint': 'eu-vision.googleapis.com'}

    client = vision.ImageAnnotatorClient(client_options=client_options)
    # [END vision_set_endpoint]
    image_source = vision.ImageSource(image_uri=image_url)
        #image_uri='gs://cloud-samples-data/vision/text/screen.jpg')
        #image_uri='https://www.wikihow.com/images/thumb/0/02/Write-a-Prescription-Step-15.jpg/aid5679943-v4-1200px-Write-a-Prescription-Step-15.jpg')
    image = vision.Image(source=image_source)

    #response = client.text_detection(image=image)
    
    response = client.document_text_detection(image=image)

    texts = []
    print('Texts:')
    
    #print('lines',len(response.text_annotations))
    #for text in response.text_annotations:
        
    #for page in response.full_text_annotation.pages: 
        
        #for block in page.blocks:
            
             
            #for paragraph in block.paragraphs:
                #texts.append(paragraph.property)
                #word_text = ""
                #for word in paragraph.words:
                    #word_text = word_text +"\n"+ ''.join([
                        #symbol.text for symbol in word.symbols])
            
                #texts.append(word_text)
                
    breaks = vision.TextAnnotation.DetectedBreak.BreakType
    paragraphs = []
    lines = []

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                para = ""
                line = ""
                for word in paragraph.words:
                    for symbol in word.symbols:
                        line += symbol.text
                        if symbol.property.detected_break.type_ == breaks.SPACE:
                            line += ' '
                        if symbol.property.detected_break.type_ == breaks.EOL_SURE_SPACE:
                            line += ' '
                            lines.append(line)
                            para += line
                            line = ''
                        if symbol.property.detected_break.type_ == breaks.LINE_BREAK:
                            lines.append(line)
                            para += line
                            line = ''
                paragraphs.append(para)                    
        #print('{}'.format(text.description))
        
        #texts.append(text.description)

        #vertices = ['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices]

        #print('bounds: {}\n'.format(','.join(vertices)))
        
    print(lines)        
        
   # lines = []
   #line =""
    #for text in texts:
        
        #for lin in text.split('\n'):
            #lines.append(lin)
        #line= line + text;
        
        #if '\n' in text:
        #    lines.append(line)
        #    line=""
    #print("number of lines",len(lines))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    context = {'texts':lines}
    return render(request, 'notes/scanp.html', context) 


def video(request):
   
    context = {}
    #return render(request, 'http://localhost:5000', context) 
    
    return redirect("http://localhost:5000")

def savenotes(request):
   
    context = {}
    return render(request, 'notes/Feeds_display.html', context) 

def main(request):
    #notes = Note.objects
    #template = loader.get_template('main.html')
    #form = ProfileForm(request.POST or None)
    #if form.is_valid():
    #    save_it = form.save(commit=False)
    #    save_it.save() 
    #context = {'notes': notes,'form': form}
    print(request.session['user_token'])
    try:
       profile = get_object_or_404(Profile, id= request.session['user_token'])
    
       print(profile.fname)
       context = {'first_name':profile.fname,
                  'last_name': profile.lname,
                  'country': profile.country,
                  'picture': profile.picture}
       return render(request, 'notes/main.html', context)

    except Exception as exception:
       context ={}
       return render(request, 'notes/main.html', context)

def resume(request):
    #notes = Note.objects
    #template = loader.get_template('upload_profile.html')
    #form = ProfileForm(request.POST or None)
    #if form.is_valid():
    #    save_it = form.save(commit=False)
    #    save_it.save() 
    #context = {'notes': notes,'form': form}
    
    context ={}
    return render(request, 'notes/upload_profile.html', context)

def signup(request):
    """
    sign up page call
    Parameters
    ----------
    request : HttpRequest
         request object

    Returns
    -----------
     HttpResponse
        content is the result of render method     
    """

    template_name = 'notes/register.html'
    #context = {'channels': channels}
    # context_object_name = 'channels'
    return render(request, template_name)  

def register(request):
    """
    sign in - sign up processing
    Parameters
    ----------
    request : HttpRequest
         request object

    Returns
    -----------
     HttpResponse
        content is the result of render method     
    """
    username = request.POST['useremail']
    password = request.POST['password']
    confirmPassword = request.POST['confirmPassword']
    print("password, confirmPassword",password,confirmPassword)

 
    error_confirm_password = None
    error_username = None
    error_password = None
     #template_name = 'nlp/signup.html'

    error_username = _validate_username(username)
    error_password, error_confirm_password = _validate_password(password,confirmPassword)
       
    if error_username == None and error_password == None and error_confirm_password == None:
       if password == confirmPassword:
               #print("password is equal to confirmPassword") 
          user = AIUser(username=username,password=password)
          user.save()

          template_name = 'notes/login.html'
       else :
               #error_confirm_password = "password and confirm password do not match"
          template_name = 'notes/register.html'
    else : 
          template_name = 'notes/register.html'     
      
    context = {'error_confirm_password': error_confirm_password,
                'error_useremail': error_username,
                'error_password': error_password
                }
    return render(request, template_name,context)


def authenticate(request):
    """
    page authentication
    Parameters
    ----------
    request : HttpRequest
         request object

    Returns
    -----------
     HttpResponse
        content is the result of render method     
    """

    print("authenticating")
    username = request.POST['useremail']
    password = request.POST['password']

    
 
    logger.info("authenticate username "+username )

    error_password = None
    try:
       user = get_object_or_404(AIUser, username=username)
    except Exception as exception:
        print(str(exception))
        template_name = 'notes/login.html'
        error_username = "Invalid username"
        context = {'error_useremail': error_username,
                'error_password': error_password}
        return render(request, template_name,context)   

    if user:
       check, error_username, error_password = user.authenticate(username, password)
       print(check,error_username,error_password)
       if check:
              request.session["user_token"] = user.id
              template_name = 'notes/Feeds_display.html'
              logger.info("authenticated username "+username)
       else :
           print("setting template as login") 
           template_name = 'notes/login.html'
           logger.info("authenticate failure username "+username )
    else :
        print("setting template as login")
        template_name = 'notes/login.html'
        error_username = "Invalid username"
        logger.info("validation failure username "+username )
        
    context = {'error_useremail': error_username,
                'error_password': error_password}
    
    return render(request, template_name,context)    



def _validate_username(username):
    error_username = None    
    if username == None:
       error_username = "user email is blank"
        
    if "@" not in username or "." not in username :
       error_username = "user email is not valid"         
    return error_username



def _validate_password(password,confirm_password):
    error_password = None
    error_confirm_password = None
    if password == None:
       error_password = "password is blank"
    if confirm_password == None:
       error_confirm_password = "confirm password is blank"
    if password != None and confirm_password != None:
       if password == confirm_password:
          error_password = None
          error_confirm_password = None
       else :
          error_password = "password and confirm_password do not match"
          error_confirm_password = "password and confirm_password do not match"   
    return error_password, error_confirm_password 


from .forms import ProfileForm
from .models import Profile

def SaveProfile(request):
       
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      print("this profile form is ",MyProfileForm.is_valid())
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.fname = MyProfileForm.cleaned_data["fname"] 
         profile.lname = MyProfileForm.cleaned_data["lname"] 
         profile.country = MyProfileForm.cleaned_data["country"] 
         #profile.picture = MyProfileForm.cleaned_data["picture"]
         print(request.session['user_token'] )
         user = get_object_or_404(AIRecruiterUser, id=int(request.session['user_token']))
         profile.userid = user 
         try:    
            profile.save()
            print("saving")
            saved = True
         except Exception as exception:
            print(str(exception))
      else:
        print("form is not valid")
        print(MyProfileForm.errors.as_text()) 
   else:
      MyProfileForm = Profileform()
        
   if saved:
      print("picture saved")
   else:
      print("Error in saving")
   #notes = Note.objects
   #template = loader.get_template('index.html')
   #form = NoteForm(request.POST or None)
   #if form.is_valid():
   #        save_it = form.save(commit=False)
   #        save_it.save() 
   #context = {'notes': notes,'form': form}
   context = {}
		
   return render(request, 'notes/index.html', context)

