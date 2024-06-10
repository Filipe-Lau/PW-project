var image = [
    "url('https://t3.ftcdn.net/jpg/05/30/11/14/360_F_530111474_fZUf6DIMCOgvtkCfJHWLZVvagcdMQnvG.jpg')",
    "url('https://files.123freevectors.com/wp-content/original/152951-abstract-black-background-vector-illustration.jpg')"
];

document.getElementById('myicon').addEventListener('click', function() {
    if (this.dataset.mode === "OFF") {
        this.dataset.mode = "ON";
        document.body.style.backgroundImage = image[1]; // Modo ON (dark mode)
        this.classList.remove('fa-moon');
        this.classList.add('fa-sun');
    } else {
        this.dataset.mode = "OFF";
        document.body.style.backgroundImage = image[0]; // Modo OFF (light mode)
        this.classList.remove('fa-sun');
        this.classList.add('fa-moon');
    }
});