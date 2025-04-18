alert("                          |Welcome to the Nigerian Election Portal|");
let year = prompt("What year is it? ");

if (year === "2027"){
    alert("It is Election Year!");
    alert("Proceed to Vote");
    age = parseInt(prompt("How old are you? "));

    if (age >=  18){
        alert("Go ahead and cast your vote!");
    }else{
        alert("Sorry, you are not eligible to vote. Try again next year.");
    }
    
}
else{
    alert("It is not election year yet. Kindly check back next year.");
}


