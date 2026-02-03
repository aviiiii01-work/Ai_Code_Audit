const faqHeaders = document.querySelectorAll('.faq-header');

faqHeaders.forEach(header => {
  header.addEventListener('click', () => {
    const parent = header.parentElement;
    const icon = header.querySelector('.icon');

    // Close all others
    document.querySelectorAll('.faq').forEach(faq => {
      if (faq !== parent) {
        faq.classList.remove('active');
        faq.querySelector('.icon').textContent = '▶';
      }
    });

    // Toggle current
    parent.classList.toggle('active');
    icon.textContent = parent.classList.contains('active') ? '▼' : '▶';
  });
});
