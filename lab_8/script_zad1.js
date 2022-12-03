//form Reprezentuje okno (dialogowe), które tworzą interfejs użytkownika aplikacji.
function Form(){   //name of the form to be printed 
    let selectForm  = document.forms[0].elements;
    window.alert(selectForm[0].value + " " + selectForm[1].value); //Getting an element from within a form
}       

function onLoader(){  // tu przy ładowaniu
    window.alert('Po załadowaniu strony!');
}