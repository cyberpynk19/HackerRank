
function aVeryBigSum($ar) {
    // Write your code here
    $soma = 0;
    for ($i = 0; $i < count($ar); $i++) {
        $soma += $ar[$i];
    }
    return $soma;
}