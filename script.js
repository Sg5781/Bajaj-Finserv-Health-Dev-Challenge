document.getElementById('data-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const jsonData = document.getElementById('json-input').value;

    try {
        const response = await fetch('https://bajaj-finserv-health-dev-challenge-e9zo.onrender.com', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: jsonData,
        });
        const result = await response.json();
        document.getElementById('result').innerText = JSON.stringify(result, null, 2);
    } catch (error) {
        document.getElementById('result').innerText = 'Error: ' + error.message;
    }
});
