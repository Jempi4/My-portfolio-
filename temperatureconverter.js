function CtoK(){
    let C = parseInt(prompt("Enter the temperature in Celsius:" ))
    K = C + 273;

    return K + "K";

    
}

function KtoC(){
    let K = parseInt(prompt("Enter the temperature in Kelvin:" ))
    C = K - 273;

    return C + "C"; 
}

function FtoC(){
    let Fahrenheit = parseInt(prompt("Enter the temperature in Fahrenheit: " ))
    C = (5/9) * (Fahrenheit - 32);

    return C + "C";

}

function CtoF(){
    let C = parseInt(prompt("Enter the temperature in Fahrenheit: " ))
    Fahrenheit = C*(9/5) + 32;

    return Fahrenheit + "F";

}



alert("Welcome to the Temperature Converter Program!")
alert("Let's get started =>")



option = prompt("Enter the option number below\n1)  Celsius to Kelvin\n2)  Kelvin to Celsius\n3)  Fahrenheit to Celsius\n4)  Celsius to Fahrenheit")

if (option === "1"){
    let tem = CtoK();
    alert("The temperature is " + tem);
} 

else if (option === "2"){
    let tem = KtoC();
    alert("The temperature is " + tem);
} 

else if (option === "3"){
    let tem = FtoC();
    alert("The temperature is " + tem);
} 

else if (option === "4"){
    let tem = CtoF();
    alert("The temperature is " + tem);
} 


else {
    alert("You must enter a valid temperature");
}

