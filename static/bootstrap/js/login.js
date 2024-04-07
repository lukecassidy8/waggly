document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('loginForm').addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/login', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                if (response.user_type) {
                    document.getElementById('userType').innerText = response.user_type;
                } else {
                    alert(response.message);
                }
            } else {
                alert('Request failed. Please try again later.');
            }
        };
        xhr.send(new URLSearchParams(formData).toString());
    });
});
