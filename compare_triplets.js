function compareTriplets(a, b) {

    let alice_score = 0;
    let bob_score = 0;


    for(let i = 0; i < a.length; i++) {
        if(a[i] > b[i]) {
            alice_score += 1;
        }
        
        if (a[i] < b[i]) {
            bob_score += 1;
        }        
        }

    return [alice_score , bob_score];    
}

const a = [1,2,3]
const b = [3,2,1]

console.log(compareTriplets(a,b))