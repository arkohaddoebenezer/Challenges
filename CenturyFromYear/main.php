<?php

class Main {
    public function getCentury($year) {
        return (int) ceil($year / 100);
    }
}

$myObject = new Main();
$year = 2024;
$century = $myObject->getCentury($year);

echo "Year: $year is in the $century" . "th century." . PHP_EOL;

?>