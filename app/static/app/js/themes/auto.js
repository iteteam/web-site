let nav = document.getElementById('navbar')
let main = document.getElementById('main')

function remove(selector, added, removed = '') {
    document.querySelectorAll(selector).forEach(
        function (element) {
            if (removed !== '') {
                element.classList.remove(removed)
            } else {
                element.classList.remove(selector)
            }
            element.classList.add(added)
        }
    )
}

function add(selector, added) {
    document.querySelectorAll(selector).forEach(
        function (element) {
            element.classList.add(added)
        }
    )
}

function addList(selector, addedList) {
    document.querySelectorAll(selector).forEach(
        function (element) {
            for (let i = 0; i < addedList.length; i++) {
                element.classList.add(addedList[i])
            }
        }
    )
}

function autoTheme() {
    let now = new Date()
    if (now.getHours() >= 19 || (now.getHours() >= 0 && now.getHours() <= 7)) {
        try {
            nav.classList.remove('bg-gradient-primary')
            nav.classList.add('bg-black')
            main.classList.add('bg-dark', 'text-white')
            addList('.form-control', ['bg-dark', 'text-white'])
            remove('.text-dark', 'text-white', 'text-dark')
            remove('.btn-soft-success', 'btn-outline-success', 'btn-soft-success')
            remove('.btn-soft-danger', 'btn-outline-danger', 'btn-soft-danger')
            remove('.badge-primary', 'badge-secondary', 'badge-primary')
            remove('.text-primary', 'text-secondary', 'text-primary')
            add('.dropdown-menu', 'dropdown-menu-inverse')
            add('.sidebar', 'bg-dark')
            remove('.message', 'bg-gradient-dark', 'bg-gradient-secondary')
        } catch (e) {

        }
    } else {
        try {
            nav.classList.remove('navbar-dark', 'bg-gradient-primary')
            nav.classList.add('navbar-light', 'bg-gradient-secondary')
            remove('.btn-soft-success', 'btn-secondary', 'btn-soft-success')
            remove('.badge-primary', 'badge-secondary', 'badge-primary')
            remove('.text-primary', 'text-secondary', 'text-primary')
            remove('.btn-soft-danger', 'btn-soft-warning', 'btn-soft-danger')
        } catch (e) {

        }
    }
}

autoTheme()