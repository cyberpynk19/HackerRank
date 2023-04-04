function plusMinus($arr) {
    $n = count($arr);
    $positive = 0;
    $negative = 0;
    $zero = 0;
    foreach ($arr as $i) {
        if ($i < 0) {
            $negative += 1;
        } elseif ($i > 0) {
            $positive += 1;
        } else {
            $zero += 1;
        }
    }
    $Ppositive = $positive / $n;
    $Pnegative = $negative / $n;
    $Pzero = $zero / $n;
    echo $Ppositive . "\n" . $Pnegative . "\n" . $Pzero . "\n";
}

$arr = array(-4, 3, -9, 0, 4, 1);
plusMinus($arr);