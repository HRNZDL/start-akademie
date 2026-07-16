function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('start_theme', newTheme);
    
    const icon = document.getElementById('theme-icon');
    if (icon && window.lucide) {
        if (newTheme === 'light') {
            icon.setAttribute('data-lucide', 'moon');
        } else {
            icon.setAttribute('data-lucide', 'sun');
        }
        lucide.createIcons();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Force light theme by default for the new corporate identity
    const savedTheme = localStorage.getItem('start_theme') || 'light';
    
    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        const icon = document.getElementById('theme-icon');
        if (icon) {
            icon.setAttribute('data-lucide', 'moon');
        }
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        const icon = document.getElementById('theme-icon');
        if (icon) {
            icon.setAttribute('data-lucide', 'sun');
        }
    }
});
