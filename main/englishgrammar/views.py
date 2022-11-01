import sys

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from subprocess import run, PIPE

from .models import getGram1


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def button(request):
    return render(request, 'home.html')


def external(request):
    # getGram1.objects.create(PoS="noun", count=0)  # id 1
    # getGram1.objects.create(PoS="preposition", count=0)  # id 2
    # getGram1.objects.create(PoS="adjective", count=0)  # id 3
    # getGram1.objects.create(PoS="verb", count=0)  # id 4
    # getGram1.objects.create(PoS="pronoun", count=0)  # id 5
    # getGram1.objects.create(PoS="conjunction", count=0)  # id 6
    # getGram1.objects.create(PoS="determiner", count=0)  # id 7
    # getGram1.objects.create(PoS="ERROR_not_found", count=0)  # id 8
    # getGram1.objects.create(PoS="sens", count=0)  # id 9
    # getGram1.objects.create(PoS="words", count=0)  # id 10
    inp = request.POST.get('param')
    if inp is not None:
        out = run([sys.executable, '//Users//jamesbrady//Desktop//djang_proj//Parser.py', inp], shell=False, stdout=PIPE)
        entry = inp
        out = str(out.stdout)
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        x = 0
        z = 1

        # adding a +1 to each Part of Speech model that was detected by the Parsimonious Parser program
        # 1-8 PoS models with count int variables, these counts will increase each time they are detected
        # in a try except to try and catch if the user does not have 1-8 objects in the getGram1 database.
        y = getGram1.objects.get(id=9)  # sentence count
        x += 1
        y.count = y.count + x
        y.save()

        words = getGram1.objects.get(id=10)

        a1 = getGram1.objects.get(id=1)
        b1 = getGram1.objects.get(id=2)
        c1 = getGram1.objects.get(id=3)
        d1 = getGram1.objects.get(id=4)
        e1 = getGram1.objects.get(id=5)
        f1 = getGram1.objects.get(id=6)
        g1 = getGram1.objects.get(id=7)
        h1 = getGram1.objects.get(id=8)
        if "Node called \"noun\"" in out:
            a = out.count("Node called \"noun\"")
            a1.count = a1.count + a
            a1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"preposition\"" in out:
            b = out.count("Node called \"preposition\"")
            b1.count = b1.count + b
            b1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"adjective\"" in out:
            c = out.count("Node called \"adjective\"")
            c1.count = c1.count + c
            c1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"verb\"" in out:
            d = out.count("Node called \"verb\"")
            d1.count = d1.count + d
            d1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"pronoun\"" in out:
            e = out.count("Node called \"pronoun\"")
            e1.count = e1.count + e
            e1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"conjunction\"" in out:
            f = out.count("Node called \"conjunction\"")
            f1.count = f1.count + f
            f1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"determiner\"" in out:
            g = out.count("Node called \"determiner\"")
            g1.count = g1.count + g
            g1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "RegexNode called \"ERROR_not_found\"" in out:
            h = out.count("called \"ERROR_not_found\"")
            h1.count = h1.count + h
            h1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()

    return render(request, 'dashboard.html', {'data1': out, 'data2': a1.count, 'data3': b1.count,
                                              'data4': c1.count, 'data5': d1.count, 'data6': e1.count,
                                              'data7': f1.count, 'data8': g1.count, 'data9': h1.count,
                                              'data10': entry, 'data12': y.count, 'data13': words.count})


def filternal(request): # if user enters file
    #getGram1.objects.create(PoS="noun", count=0)  # this is here incase the database is missing 1-10 objects, id must be 1-10
    #getGram1.objects.create(PoS="preposition", count=0)  # id 2
    #getGram1.objects.create(PoS="adjective", count=0)  # id 3
    #getGram1.objects.create(PoS="verb", count=0)  # id 4
    #getGram1.objects.create(PoS="pronoun", count=0)  # id 5
    #getGram1.objects.create(PoS="conjunction", count=0)  # id 6
    #getGram1.objects.create(PoS="determiner", count=0)  # id 7
    #getGram1.objects.create(PoS="ERROR_not_found", count=0)  # id 8
    #getGram1.objects.create(PoS="sens", count=0)  # id 9
    #getGram1.objects.create(PoS="words", count=0)  # id 10
    inp = request.POST.get('param1')
    if inp is not None:
        string = '/Users/jamesbrady/Desktop/'+inp
        f = open(string, 'r')
        file_content = f.read()
        out = run([sys.executable, '//Users//jamesbrady//Desktop//djang_proj//Parser.py', file_content], shell=False, stdout=PIPE)
        entry = file_content
        out = str(out.stdout)
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        x = 0
        z = 0

        # adding a +1 to each Part of Speech(getGram1) model that was detected by the Parsimonious Parser program
        # 1-8 PoS models with count int variables, these counts will increase each time they are detected
        # in a try except to try and catch if the user does not have 1-8 objects in the getGram1 database.
        y = getGram1.objects.get(id=9)  # sentence count
        x += 1
        y.count = y.count + x
        y.save()

        words = getGram1.objects.get(id=10)

        a1 = getGram1.objects.get(id=1)
        b1 = getGram1.objects.get(id=2)
        c1 = getGram1.objects.get(id=3)
        d1 = getGram1.objects.get(id=4)
        e1 = getGram1.objects.get(id=5)
        f1 = getGram1.objects.get(id=6)
        g1 = getGram1.objects.get(id=7)
        h1 = getGram1.objects.get(id=8)
        if "Node called \"noun\"" in out:
            a = out.count("Node called \"noun\"")
            a1.count = a1.count + a
            a1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"preposition\"" in out:
            b = out.count("Node called \"preposition\"")
            b1.count = b1.count + b
            b1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"adjective\"" in out:
            c = out.count("Node called \"adjective\"")
            c1.count = c1.count + c
            c1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"verb\"" in out:
            d = out.count("Node called \"verb\"")
            d1.count = d1.count + d
            d1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"pronoun\"" in out:
            e = out.count("Node called \"pronoun\"")
            e1.count = e1.count + e
            e1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"conjunction\"" in out:
            f = out.count("Node called \"conjunction\"")
            f1.count = f1.count + f
            f1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "Node called \"determiner\"" in out:
            g = out.count("Node called \"determiner\"")
            g1.count = g1.count + g
            g1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()
        if "RegexNode called \"ERROR_not_found\"" in out:
            h = out.count("called \"ERROR_not_found\"")
            h1.count = h1.count + h
            h1.save()
            z = 0
            z += 1
            words.count = words.count + z
            words.save()

    return render(request, 'dashboard.html', {'data1': out, 'data2': a1.count, 'data3': b1.count,
                                          'data4': c1.count, 'data5': d1.count, 'data6': e1.count,
                                          'data7': f1.count, 'data8': g1.count, 'data9': h1.count,
                                          'data10': entry, 'data12': y.count, 'data13': words.count})