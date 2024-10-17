// JavaScript for adding interactivity

// Smooth scroll for navigation links
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        const sectionId = this.getAttribute('href').slice(1);
        document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
    });
});

// Function to animate features section
window.addEventListener('scroll', function() {
    const features = document.querySelector('.features');
    const featuresPosition = features.getBoundingClientRect().top;
    const screenPosition = window.innerHeight / 1.3;

    if (featuresPosition < screenPosition) {
        features.classList.add('features-animate');
    }
});
