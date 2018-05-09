// Day 1: Functions

/*
 * Create the function factorial here
 */

function factorial(n){
    if (n==1){
        return n;
    } else{
        return n * factorial(n-1);
    }
}