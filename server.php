<?php
// Define a dataset containing a list of names and ages
$dataset = array(
  array('name' => 'Alice', 'age' => 25),
  array('name' => 'Bob', 'age' => 30),
  array('name' => 'Charlie', 'age' => 35)
);

// Define a function to handle incoming requests
function handle_request($method, $path) {
  global $dataset;

  // Check if the request is a GET request
  if ($method == 'GET') {
    // If the request path is "/data", return the entire dataset as JSON
    if ($path == '/data') {
      header('Content-Type: application/json');
      echo json_encode($dataset);
      return;
    }

    // If the request path is "/data/<name>", find the matching record and return it as JSON
    if (preg_match('/^\/data\/(\w+)$/', $path, $matches)) {
      $name = $matches[1];
      foreach ($dataset as $record) {
        if ($record['name'] == $name) {
          header('Content-Type: application/json');
          echo json_encode($record);
          return;
        }
      }
      header('HTTP/1.1 404 Not Found');
      return;
    }
  }

  if ($method == 'POST') {
    // If the request path is "/upload", handle the video upload
    echo json_encode(array('status' => 'pass post', 'message' => 'pass post'));
    if ($path == '/upload') {
        echo json_encode(array('status' => $_FILES, 'message' => 'pass upload'));
      // Check if the video was successfully uploaded
      if (isset($_FILES['video'])) {
        echo json_encode(array('status' => $_FILES, 'message' => 'pass video'));
        // Get the temporary filename of the uploaded video
        $tmp_name = $_FILES['video']['tmp_name'];

        // Move the uploaded video to a permanent location on the server
        $filename = uniqid() . '.mp4'; // Generate a unique filename for the video
        $upload_dir = 'uploads/'; // Specify the directory where uploaded files will be stored
        move_uploaded_file($tmp_name, $upload_dir . $filename);

        // Return a success response with the URL of the uploaded video
        header('Content-Type: application/json');
        echo json_encode(array('status' => 'success', 'url' => $upload_dir . $filename));
        return;
      } else {
        // Return an error response if the video was not uploaded successfully
        header('HTTP/1.1 400 Bad Request');
        header('Content-Type: application/json');
        echo json_encode(array('status' => 'error', 'message' => 'Error uploading video'));
        return;
      }
    }

  // If the request is not a GET request or the path is not recognized, return a 404 error
  header('HTTP/1.1 404 Not Found');
}
}

// Define the server address and port
$host = 'localhost';
$port = 8000;

// Start the server and listen for incoming requests
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($socket, $host, $port);
socket_listen($socket);

// Print a message indicating that the server is running
echo "Server running at http://$host:$port\n";

// Handle incoming requests
while (true) {
  $client = socket_accept($socket);
  $request = socket_read($client, 1024);
  list($method, $path, $version) = explode(' ', $request);
  handle_request($method, $path);
  socket_close($client);
}
?>