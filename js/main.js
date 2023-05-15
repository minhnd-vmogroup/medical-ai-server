function getData() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            const resultElement = document.getElementById('result');
            resultElement.innerHTML = `Server says: ${data.message}`;
        });
}