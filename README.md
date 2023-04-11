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


Hello!

Here I have added the final project in 2 variants: archived and unarchived.

Prerequisites for running the project:

• Install Google Chrome

• Install Pycharm Community Edition: https://www.jetbrains.com/pycharm/download

• Install Python: https://www.python.org/downloads/

Instructions for running the project:

• Download the project to a location on your PC where the prerequisites have been installed.

• Open the IDE (Pycharm)>>File>>Open>>choose the project from the location where it was downloaded. After the project is loaded in the IDE, select a Python interpreter.

Instructions for running automated project tests:

We need a Python library that implements Gherkin syntax: [behave]. We also need the selenium webdriver-manager and a library for generating reports [behave-html-formatter].

• Open a terminal (venv) and install the libraries using pip install:

pip install behave/python.exe -m pip install --upgrade pip (upgrade pip only if needed)

pip install selenium

pip install webdriver-manager

pip install behave-html-formatter

• After installing the libraries, execute the command in the terminal: behave to start the automated testing.

• To generate an html report as well: In the terminal (venv): behave -f html -o name_report.html (name = we can add whatever name we want).

The developed project tests the main functionalities of the web page: https://the-internet.herokuapp.com: home page, login page, and secure page (update - background, @smoke, and Scenario outline) using behavior-driven development: BDD (Behavior Driven Development)-Selenium, POM (Page Object Model), Behave Python framework, and the Gherkin language for writing scenarios.

Automated testing is important because it helps us quickly and efficiently identify errors or defects in the developed software.

This allows programmers to validate their code and ensure that all software functionalities are working as they should.

Advantages of automated testing: Speed, Efficiency, Reliability.













