// Day 2: Conditional Statements: Switch


function getLetter(s) {
    switch(s.charAt(0)) {
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        return "A";
        break;
    case "b":
    case "c":
    case "d":
    case "f":
    case "g":
        return "B";
        break;
    
    case "h":
    case "j":
    case "k":
    case "l":
    case "m":
        return "C";
        break;
    default:
        return "D";
        break;
    } 
}