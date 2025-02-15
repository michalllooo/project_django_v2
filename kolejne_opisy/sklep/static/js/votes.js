document.addEventListener('DOMContentLoaded', function() {
    const voteButtons = document.querySelectorAll('.vote-button');

    voteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const cityName = this.getAttribute('data-city');

            fetch('/vote_city/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ city_name: cityName })
            })
            .then(response => response.json())
            .then(data => {
                if (data.votes !== undefined) {
                    const voteElement = document.getElementById(`votes-${cityName.toLowerCase()}`);
                    if (voteElement) {
                        voteElement.innerText = data.votes;
                    }
                    voteButtons.forEach(btn => btn.classList.remove('selected'));
                    this.classList.add('selected');
                } else if (data.error) {
                    alert(data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}