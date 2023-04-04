function miniMaxSum(arr) {
    // Write your code here
    let sum = 0;
    let max = -Infinity;
    let min = Infinity;
    for(let i = 0; i < arr.length; i++) {
        let numero = arr[i];
        sum += numero;
        if (numero > max) {
            max = numero;
        }
        if (numero < min) {
            min = numero;
        }
    }

    let minSum = sum - max
    let maxSum = sum - min

    console.log(minSum +" "+ maxSum)

}
arr = [1,3,5,7,9]
miniMaxSum(arr)