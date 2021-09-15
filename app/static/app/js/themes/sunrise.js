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

function sunRise() {
    try {
        nav.classList.remove('navbar-dark', 'bg-gradient-primary')
        nav.classList.add('navbar-light', 'bg-gradient-warning')
        add('main a', 'text-warning')
        normalizeAnchors('text-warning')
        remove('.badge-primary', 'badge-warning', 'badge-primary')
        remove('.btn-soft-success', 'btn-soft-warning', 'btn-soft-success')
        remove('.btn-soft-danger', 'btn-outline-warning', 'btn-soft-danger')
        remove('.text-primary', 'text-warning', 'text-primary')
    } catch (e) {
    }
}


sunRise()