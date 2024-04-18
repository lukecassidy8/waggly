document.addEventListener('DOMContentLoaded', function() {
    function showUserType() {
        fetch('/getUserType')
            .then(response => response.json())
            .then(data => {
                if (data.userType) {
                    document.getElementById("userType").innerText = data.userType;
                    if (data.userType === "dogOwner") {
                        fetch('/getNumberOfDogs')
                            .then(response => response.json())
                            .then(data => {
                                if (data.numberOfDogs != null) {
                                    document.getElementById("numberOfDogs").innerText = `Number of Dogs: ${data.numberOfDogs}`;
                                } else {
                                    document.getElementById("numberOfDogs").innerText = "Number of Dogs: 0";
                                }
                            })
                            .catch(error => {
                                console.error('Error:', error);
                            });
                    } else {
                        document.getElementById("numberOfDogs").innerText = "Number of Dogs: N/A";
                    }
                } else {
                    document.getElementById("userType").innerText = "User type not found";
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    showUserType();

    document.getElementById('logoutBtn').addEventListener('click', function(){
        fetch('/logout')
        .then(response=> response.json())
        .then(data=>{
            if(data.success){
                window.location.href = '/';
            }else{
                console.error('Logout failed', data.message);
            }
        })
        .catch(error=>{
            console.error('Error', error)
        })
    })
});
