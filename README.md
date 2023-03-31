# FinalProject
Buna ziua!

Aici am adaugat proiectul final in 2 variante: arhivat si nearhivat.

Precondiții pentru rulare proiect:

• Instalați Google Chrome

• Instalați Pycharm Community Edition: https://www.jetbrains.com/pycharm/download

• Instalați Python: https://www.python.org/downloads/

Instrucțiuni pentru rulare proiect:

• Se descarcă proiectul intr-o locație a PC-ului in care s-au instalat cele menționate la precondiții.

• Se deschide IDE-ul (Pycharm)>>File>>Open>>se alege proiectul din locația in care s-a descărcat, după incărcare proiect in IDE se alege un Python interpreter. 

Instrucțiuni pentru rulare teste automate proiect:

Avem nevoie de o bibliotecă Python care implementează sintaxa Gherkin: [behave]
Avem nevoie, de asemenea, de selenium webdriver-manager și o bibliotecă pentru generarea rapoartelor [behave-html-formatter].

• Se deschide un terminal(venv) și se instalează cu pip install librărille:

-	pip install behave/python.exe -m pip install --upgrade pip(upgarde pip doar daca e nevoie)

-  pip install selenium

-	pip install webdriver-manager

-	pip install behave-html-formatter

• Dupa instalarea librăriilor tot in terminal se executa comanda: behave pentru pornirea testării automate.

• Pentru a genera si un raport.html :In terminal(venv): behave -f html -o name_report.html(name= putem adauga ce nume dorim).
   
Proiectul dezvoltat testeaza : funcționalități principale ale paginii web: https://the-internet.herokuapp.com: home page, login page si secure page(update -background, @smoke si Scenario outline) utilizand dezvoltarea orientată către comportament :BDD((Behavior Driven Development)-Selenium, POM (Page Object Model),Behave Python framework si limbajul Gherkin pentru scrierea scenariilor. 

Testarea automată este importantă pentru că ne ajută la identificarea rapidă și eficientă a erorilor sau defectelor în software-ul dezvoltat. 

Aceasta permite programatorilor să își valideze codul și să își asigure că toate funcționalitățile din software funcționează așa cum ar trebui.

Avantaje ale testării automate: Rapiditate, Eficiență, Fiabilitate.












