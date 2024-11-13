function showLoader(event) {
    console.log('Loader triggered');
    event.preventDefault();
    event.stopPropagation();

    document.getElementById('loader').style.display = 'block';
    
    setTimeout(() => {
        window.location.href = event.currentTarget.href; // Use the href from the clicked link
    }, 3000); // Delay set to 3000 milliseconds (3 seconds)
}
