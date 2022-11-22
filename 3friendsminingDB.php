<head>
  <title>3friendsmining.co | Mining simplified.</title>
</head>
<!--
<form action="" method="POST">
    <input type="text" name="firstname">
<input type="text" name="lastname">
<input type="text" name="email">
    <input type="submit">
</form>
-->

<?php
$str = file_get_contents('response.json');
$json = json_decode($str, true); // decode the JSON into an associative array
echo '<pre>' . print_r($json, true) . '</pre>';

$btc_name = $json["data"]["BTC"]["name"];
$btc_symbol = $json["data"]["BTC"]["symbol"];
$btc_price = $json["data"]["BTC"]["quote"]["USD"]["price"];
$btc_cmc_rank = $json["data"]["BTC"]["cmc_rank"];
$btc_market_dominance = $json["data"]["BTC"]["quote"]["USD"]["market_cap_dominance"];

$doge_name = $json["data"]["DOGE"]["name"];
$doge_symbol = $json["data"]["DOGE"]["symbol"];
$doge_price = $json["data"]["DOGE"]["quote"]["USD"]["price"];
$doge_cmc_rank = $json["data"]["DOGE"]["cmc_rank"];
$doge_market_dominance = $json["data"]["DOGE"]["quote"]["USD"]["market_cap_dominance"];

$etc_name = $json["data"]["ETC"]["name"];
$etc_symbol = $json["data"]["ETC"]["symbol"];
$etc_price = $json["data"]["ETC"]["quote"]["USD"]["price"];
$etc_cmc_rank = $json["data"]["ETC"]["cmc_rank"];
$etc_market_dominance = $json["data"]["ETC"]["quote"]["USD"]["market_cap_dominance"];

$eth_name = $json["data"]["ETH"]["name"];
$eth_symbol = $json["data"]["ETH"]["symbol"];
$eth_price = $json["data"]["ETH"]["quote"]["USD"]["price"];
$eth_cmc_rank = $json["data"]["ETH"]["cmc_rank"];
$eth_market_dominance = $json["data"]["ETH"]["quote"]["USD"]["market_cap_dominance"];

$rvn_name = $json["data"]["RVN"]["name"];
$rvn_symbol = $json["data"]["RVN"]["symbol"];
$rvn_price = $json["data"]["RVN"]["quote"]["USD"]["price"];
$rvn_cmc_rank = $json["data"]["RVN"]["cmc_rank"];
$rvn_market_dominance = $json["data"]["RVN"]["quote"]["USD"]["market_cap_dominance"];

$xmr_name = $json["data"]["XMR"]["name"];
$xmr_symbol = $json["data"]["XMR"]["symbol"];
$xmr_price = $json["data"]["XMR"]["quote"]["USD"]["price"];
$xmr_cmc_rank = $json["data"]["XMR"]["cmc_rank"];
$xmr_market_dominance = $json["data"]["XMR"]["quote"]["USD"]["market_cap_dominance"];

#if(isset($_POST["firstname"])){
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "3friendsminingDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO btc (btc_name,btc_symbol,btc_price,btc_cmc_rank,btc_market_dominance)
 VALUES ('".$btc_name."','".$btc_symbol."','".$btc_price."','".$btc_cmc_rank."','".$btc_market_dominance."')";

if ($conn->query($sql) === TRUE) {
    echo "BTC updated successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$sql = "INSERT INTO doge (doge_name,doge_symbol,doge_price,doge_cmc_rank,doge_market_dominance)
 VALUES ('".$doge_name."','".$doge_symbol."','".$doge_price."','".$doge_cmc_rank."','".$doge_market_dominance."')";

if ($conn->query($sql) === TRUE) {
    echo "DOGE updated successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$sql = "INSERT INTO etc (etc_name,etc_symbol,etc_price,etc_cmc_rank,etc_market_dominance)
 VALUES ('".$etc_name."','".$etc_symbol."','".$etc_price."','".$etc_cmc_rank."','".$etc_market_dominance."')";

if ($conn->query($sql) === TRUE) {
    echo "ETC updated successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$sql = "INSERT INTO eth (eth_name,eth_symbol,eth_price,eth_cmc_rank,eth_market_dominance)
 VALUES ('".$eth_name."','".$eth_symbol."','".$eth_price."','".$eth_cmc_rank."','".$eth_market_dominance."')";

if ($conn->query($sql) === TRUE) {
    echo "ETH updated successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$sql = "INSERT INTO rvn (rvn_name,rvn_symbol,rvn_price,rvn_cmc_rank,rvn_market_dominance)
 VALUES ('".$rvn_name."','".$rvn_symbol."','".$rvn_price."','".$rvn_cmc_rank."','".$rvn_market_dominance."')";

if ($conn->query($sql) === TRUE) {
    echo "RVN updated successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$sql = "INSERT INTO xmr (xmr_name,xmr_symbol,xmr_price,xmr_cmc_rank,xmr_market_dominance)
 VALUES ('".$xmr_name."','".$xmr_symbol."','".$xmr_price."','".$xmr_cmc_rank."','".$xmr_market_dominance."')";

if ($conn->query($sql) === TRUE) {
    echo "XMR updated successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
#}
?>