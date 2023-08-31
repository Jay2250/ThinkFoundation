import json
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from home.models import Data
from django.contrib.auth.models import User

from .forms import AddDataForm, SignUpForm
from django.contrib import messages



def home(request):
    with open("staticfiles/csvjson.json", 'r', encoding='utf-8') as data:
        parsed_csv = json.load(data)

    if Data.objects.all().count() == 0:
        for data in parsed_csv:
            Data.objects.get_or_create(
            polling_booth_number  = data["Polling Booth Number"],                 
            polling_booth_name    = data["Polling Booth Name"],           
            parent_constituency   = data["Parent Constituency"],           
            winner2014            = data["Winner- 2014"],
            runner_up             = data["1st Runner up other than INC and BJP"],
            margin1_percent       = data["Margin (%)"],      
            margin1               = data["Margin"],
            total_voters          = data["Total Voters"],          
            bjp1_votes            = data["BJP - Votes"],  
            bjp1_vote_percent     = data["BJP- % vote"],               
            inc1_votes            = data["INC- Votes"],
            inc1_votes_percent    = data["INC- % votes"],               
            winner2019            = data["Winner- 2019"],
            margin2_percent       = data["Margin %"],       
            margin2               = data["Margin__1"],   
            total2_voters         = data["Total Voters__1"],         
            bjp2_votes            = data["BJP- Votes"], 
            bjp2_votes_percent    = data["BJP- % votes"],               
            inc2_votes            = data["INC- Votes__1"],
            inc2_vote_percent     = data["INC- % Votes"]             
        )    
    data = Data.objects.all()
    if request.method != 'POST':
        return render(request, 'pages/home.html', {'data': data})
    username = request.POST['username']
    password = request.POST['password']
    email = User.objects.filter(username=username).values_list('email')
    status = User.objects.filter(username=username).values_list('last_name')
    print(email)
    # Authenticate
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        
        
        pc ={'karanja@karanja.com': 'Karanja', 'ashti@ashti.com': 'Ashti', 'arvi@arvi.com': 'Arvi', 'admin@admin.com': 'Admin'}
        pc = pc[email[0][0]]   
        print(pc)
        if status[0][0] == '2':
            pc = 'Complete '
        return render(request, 'pages/home.html', {'data': data, 'pc': pc})
    
    return redirect('home')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            
            user = authenticate(username=username, password=password)
                
                
            
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
# 
        return render(request, 'accounts/sign-up.html', {'form': form})
    return render(request, 'accounts/sign-up.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')


def data_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        username = request.user.username
        customer_record = Data.objects.get(id=pk)
        email = User.objects.filter(username=username).values_list('email')
        status = User.objects.filter(username=username).values_list('last_name')
        pc ={'karanja@karanja.com': 'Karanja', 'ashti@ashti.com': 'Ashti', 'arvi@arvi.com': 'Arvi', 'admin@admin.com': 'Admin'}
        pc = pc[email[0][0]]   
        print(pc)
        if status[0][0] == '2':
            pc = 'Complete '
        return render(request, 'pages/record.html', {'data':customer_record, 'pc': pc})
    else:
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_superuser:
        delete_it = Data.objects.get(id=pk)
        delete_it.delete()

    return redirect('home')


def add_record(request):
    form = AddDataForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST" and form.is_valid():
            add_record = form.save()
            return redirect('home')
        return render(request, 'pages/add_record.html', {'form': form})
    else:
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Data.objects.get(id=pk)
        form = AddDataForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'pages/update_record.html', {'form':form})
    else:
        return redirect('home')