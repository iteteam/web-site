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

function redRose() {
    try {
        nav.classList.remove('bg-gradient-primary')
        nav.classList.add('bg-gradient-red')
        add('main a', 'text-danger')
        normalizeAnchors('text-danger')
        remove('.btn-soft-success', 'btn-outline-danger', 'btn-soft-success')
        remove('.badge-primary', 'badge-danger', 'badge-primary')
        remove('.text-primary', 'text-danger', 'text-primary')
    } catch (e) {
    }
}


redRose()