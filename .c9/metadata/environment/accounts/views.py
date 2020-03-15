{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":[","],"id":73}],[{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"insert","lines":[" "],"id":74}],[{"start":{"row":3,"column":42},"end":{"row":3,"column":63},"action":"insert","lines":["UserRegistrationForm("],"id":75}],[{"start":{"row":3,"column":62},"end":{"row":3,"column":63},"action":"remove","lines":["("],"id":76}],[{"start":{"row":39,"column":0},"end":{"row":41,"column":47},"action":"remove","lines":["def registration(request):","    \"\"\"Render the registration page\"\"\"","    return render(request, 'registration.html')"],"id":77},{"start":{"row":39,"column":0},"end":{"row":44,"column":48},"action":"insert","lines":["","def registration(request):","    \"\"\"Render the registration page\"\"\"","    registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"]}],[{"start":{"row":40,"column":0},"end":{"row":44,"column":48},"action":"remove","lines":["def registration(request):","    \"\"\"Render the registration page\"\"\"","    registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"],"id":78},{"start":{"row":40,"column":0},"end":{"row":61,"column":48},"action":"insert","lines":["def registration(request):","    \"\"\"Render the registration page\"\"\"","    if request.user.is_authenticated:","        return redirect(reverse('index'))","","    if request.method == \"POST\":","        registration_form = UserRegistrationForm(request.POST)","","        if registration_form.is_valid():","            registration_form.save()","","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully registered\")","            else:","                messages.error(request, \"Unable to register your account at this time\")","    else:","        registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"]}]]},"ace":{"folds":[],"scrolltop":411.21875,"scrollleft":0,"selection":{"start":{"row":61,"column":48},"end":{"row":61,"column":48},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":27,"state":"start","mode":"ace/mode/python"}},"timestamp":1584306993130,"hash":"0da1b8a7c8ab2eda32c394ddc35507e55624598e"}