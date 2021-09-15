let nav = document.getElementById('navbar')
let main = document.getElementById('main')

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

function normalizeAnchors(klass) {
    document.querySelectorAll('main a.btn').forEach(function (e) {
        e.classList.remove(klass)
    })
}

function lightTheme() {
    try {
        nav.classList.remove('navbar-dark', 'bg-gradient-primary')
        nav.classList.add('navbar-light', 'bg-gradient-secondary')
        add('main a', 'text-secondary')
        normalizeAnchors('text-secondary')
        remove('.btn-soft-success', 'btn-secondary', 'btn-soft-success')
        remove('.badge-primary', 'badge-secondary', 'badge-primary')
        remove('.text-primary', 'text-secondary', 'text-primary')
        remove('.btn-soft-danger', 'btn-soft-warning', 'btn-soft-danger')
    } catch (e) {

    }
}

lightTheme()