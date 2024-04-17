document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('loginForm').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting normally
        const formData = new FormData(this);
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/login', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                if (response.success) {
                    // Redirect user to dashboard if login is successful
                    window.location.href = '/dashboard';
                } else {
                    // Display error message to the user
                    document.getElementById('responseMessage').innerText = response.message;
                }
            } else {
                alert('Request failed. Please try again later.');
            }
        };
        xhr.send(new URLSearchParams(formData).toString());
    });
});
