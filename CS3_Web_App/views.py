from django.shortcuts import render, redirect
from pyrebase import pyrebase

# firebase application config
config = {
    'apiKey': "AIzaSyBfTC04mTX6MhbvS61ixHrM7oFLrlwMfUY",
    'authDomain': "cs3-st.firebaseapp.com",
    'databaseURL': "https://cs3-st-default-rtdb.firebaseio.com",
    'projectId': "cs3-st",
    "storageBucket": "cs3-st.appspot.com",
    "messagingSenderId": "94001336639",
    "appId": "1:94001336639:web:442c48169e52ed0744c38a",
    "measurementId": "G-DGLQBLKH36"
}
firebase = pyrebase.initialize_app(config)
fireauth = firebase.auth()
database = firebase.database()
storage = firebase.storage()


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        try:
            fullname = request.POST['fullname']
            email = request.POST['email']
            password = request.POST['password']
            grade = request.POST['grade']
            sub_team = request.POST['sub_team']

            user = fireauth.create_user_with_email_and_password(email, password)
            uid = user['localId']

            data = {
                'uid': uid,
                'fullname': fullname,
                'email': email,
                'grade': grade,
                'sub_team': sub_team,

            }

            database.child("users").child(uid).set(data)
            return redirect('login')
        except Exception as e:
            message = "Unable to create account. Please Try again"
            print(e, message)
            return render(request, 'signup.html', {'msg': message})
    else:
        return render(request, 'signup.html')


def dashboard(request):
    email = request.POST.get('email')
    passw = request.POST.get("password")

    try:
        user = fireauth.sign_in_with_email_and_password(email, passw)
        session_id = user['idToken']
        request.session['sid'] = str(session_id)
        uid = user['localId']
        request.session['uid'] = uid
        request.session.modified = True
    except Exception as e:
        print(e)
        message = "Invalid Credentials"
        return render(request, "login.html", {"msg": message})
    return render(request, "dashboard.html", {"e": email})


def ownprofile(request):
    if request.session.get('sid'):
        uid = request.session.get('uid')
        print(uid)
        profile = database.child("users").child(uid).get().val()
        return render(request, 'ownprofile.html', {'profile': profile})
    else:
        return redirect('/login/')


def updateprofile(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        sub_team = request.POST['sub_team']
        grade = request.POST['grade']
        uid = request.session.get('uid')

        data = {
            'fullname': fullname,
            'email': email,
            'sub_team': sub_team,
            'grade': grade,
            'uid': uid,
        }

        print(data)
        database.child("users").child(uid).set(data)
    return redirect('/profile/')


def publicprofile(request, name):
    profile = database.child('users').child(name).get().val()
    return render(request, 'publicprofile.html', {'profile': profile})


def reset(request):
    return render(request, "reset.html")


def postReset(request):
    email = request.POST.get('email')
    try:
        fireauth.send_password_reset_email(email)
        message = "A email to reset password is successfully sent"
        return render(request, "reset.html", {"msg": message})
    except:
        message = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "reset.html", {"msg": message})
