{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":26,"position":26,"stack":[[{"start":{"row":3,"column":0},"end":{"row":5,"column":41},"action":"insert","lines":["def index(request):","    \"\"\"Return the index.html file\"\"\"","    return render(request,  'index.html')"],"id":2}],[{"start":{"row":5,"column":41},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":4}],[{"start":{"row":7,"column":0},"end":{"row":10,"column":37},"action":"insert","lines":["def logout(request):","    \"\"\"Log the user out\"\"\"","    auth.logout(request)","    return redirect(reverse('index'))"],"id":5}],[{"start":{"row":0,"column":35},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":31},"action":"insert","lines":["from django.contrib import auth"],"id":7}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[","],"id":8}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":[" "],"id":9},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["r"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":39},"action":"remove","lines":["re"],"id":10},{"start":{"row":0,"column":37},"end":{"row":0,"column":47},"action":"insert","lines":["redirect()"]}],[{"start":{"row":0,"column":46},"end":{"row":0,"column":47},"action":"remove","lines":[")"],"id":11}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"remove","lines":["("],"id":12}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":[","],"id":13}],[{"start":{"row":0,"column":46},"end":{"row":0,"column":47},"action":"insert","lines":[" "],"id":14},{"start":{"row":0,"column":47},"end":{"row":0,"column":48},"action":"insert","lines":["r"]},{"start":{"row":0,"column":48},"end":{"row":0,"column":49},"action":"insert","lines":["e"]},{"start":{"row":0,"column":49},"end":{"row":0,"column":50},"action":"insert","lines":["v"]}],[{"start":{"row":0,"column":47},"end":{"row":0,"column":50},"action":"remove","lines":["rev"],"id":15},{"start":{"row":0,"column":47},"end":{"row":0,"column":56},"action":"insert","lines":["reverse()"]}],[{"start":{"row":0,"column":55},"end":{"row":0,"column":56},"action":"remove","lines":[")"],"id":16},{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"remove","lines":["("]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":[","],"id":17}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":[" "],"id":18},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["m"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["e"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":36},"action":"remove","lines":["mes"],"id":19},{"start":{"row":1,"column":33},"end":{"row":1,"column":41},"action":"insert","lines":["messages"]}],[{"start":{"row":10,"column":24},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":70},"action":"insert","lines":["messages.success(request, \"You have successfully been logged out\")"],"id":21}],[{"start":{"row":12,"column":37},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":23}],[{"start":{"row":14,"column":0},"end":{"row":16,"column":40},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    return render(request, 'login.html')"],"id":24}],[{"start":{"row":14,"column":0},"end":{"row":16,"column":40},"action":"remove","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    return render(request, 'login.html')"],"id":26},{"start":{"row":14,"column":0},"end":{"row":17,"column":68},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"]}],[{"start":{"row":1,"column":41},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":40},"action":"insert","lines":["from accounts.forms import UserLoginForm"],"id":28}],[{"start":{"row":15,"column":0},"end":{"row":18,"column":68},"action":"remove","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"],"id":29},{"start":{"row":15,"column":0},"end":{"row":32,"column":68},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    if request.method == \"POST\":","        login_form = UserLoginForm(request.POST)","","        if login_form.is_valid():","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password'])","            ","","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully logged in!\")","            else:","                login_form.add_error(None, \"Your username or password is incorrect\")","    else:","        login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":12},"end":{"row":23,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584274919117,"hash":"40b24153e28330db8d5078e257e917b12caf60c2"}