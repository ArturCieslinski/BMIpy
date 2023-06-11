x = input('Wprowadź obecną masę ciała w kg\n')
y = input ('Wprowadź wzrost w m w formie n.nn\n')
bmi = float(x)/(float(y)**2)
print('BMI = ' + str(bmi))
print(
    'mniej niż 16 - wygłodzenie \n'
    '16 - 16.99 - wychudzenie \n'
    '17 - 18.49 - niedowaga \n'
    '18.5 - 24.99 - wartość prawidłowa \n'
    '25 - 29.99 - nadwaga \n'
    '30 - 34.99 - I stopień otyłości \n'
    '35 - 39.99 - II stopień otyłości \n'
    'powyżej 40 - otyłość skrajna')
print('Aby zamknąć okno naciśnij ENTER')
input()
