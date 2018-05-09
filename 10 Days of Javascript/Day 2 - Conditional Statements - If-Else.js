// Day 2: Conditional Statements: If-Else

function getGrade(score) {
    let grade;
    if (score>25){
        return "A";
    } else if (score>20){
        return "B";
    } else if (score >15){
        return "C";
    } else if (score >10){
        return "D";
    }else if (score >5){
        return "E";
    }else{
        return "F";
    }
}