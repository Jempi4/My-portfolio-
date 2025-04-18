let score = parseInt(prompt("Enter your score for grading"));

if (score > 100){
    alert("Enter a valid score");
}else if (score >= 70){
    alert("Your Grade score:" + " " + score + " " + "is grade A.");
}else if (score >= 60){
    alert("Your score: " + score + " " + "is grade B.");
}else if(score >= 50){
    alert("Your score: " + score + " " + "is grade C.");
}else if (score >= 40){
    alert("Your score: " + score + " " + "is grade D.");
}else{
    alert("You failed!");
}