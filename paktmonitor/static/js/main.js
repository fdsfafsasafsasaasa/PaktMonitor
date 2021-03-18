setTimeout( function () {
    fetch('/api/appliances/status')
        .then((response) => response.json())
        .then((data) => console.log(data))
    }, 5000)