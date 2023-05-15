<?php
// Check if the request method is POST
$GLOBALS['server'] = "http://localhost/8000";
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  // Get the string data from the request body
  $string = $_POST['string'];

  // Do something with the string data, like store it in a database or file
  // ...

  // Return a response to the client
  header('Content-Type: application/json');
  echo json_encode(array('status' => 'success'));
} else {
  // Return an error response if the request method is not POST
  header('HTTP/1.1 405 Method Not Allowed');
  header('Allow: POST');
  echo "Method not allowed.";
}
?>