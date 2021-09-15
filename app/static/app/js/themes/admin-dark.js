function adminDark() {
    document.getElementById('main').classList.add('text-white')
    document.querySelectorAll('.navbar').forEach(function (e) {
        e.classList.remove('navbar-light', 'bg-white');
        e.classList.add('navbar-dark', 'bg-black')
    })
    document.querySelectorAll('.dropdown-menu').forEach(function (e) {
        e.classList.add('dropdown-menu-inverse')
    })
    document.querySelectorAll('.bg-white').forEach(function (e) {
        e.classList.remove('bg-white');
        e.classList.add('bg-black');
    })
    document.querySelectorAll('.bg-gradient-secondary').forEach(function (e) {
        e.classList.remove('bg-gradient-secondary');
        e.classList.add('bg-dark');
    })
    document.querySelectorAll('.navbar-light').forEach(function (e) {
        e.classList.remove('navbar-light');
        e.classList.add('navbar-dark');
    })
}

adminDark()