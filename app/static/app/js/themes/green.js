let nav = document.getElementById('navbar')
let main = document.getElementById('main')

function add(selector, added) {
    document.querySelectorAll(selector).forEach(
        function (element) {
            element.classList.add(added)
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

function greenPlant() {
    try {
        nav.classList.remove('bg-gradient-primary')
        nav.classList.add('bg-gradient-green')
        add('main a', 'text-success')
        normalizeAnchors('text-success')
        remove('.btn-soft-danger', 'btn-outline-success', 'btn-soft-danger')
        remove('.badge-primary', 'badge-success', 'badge-primary')
        remove('.text-primary', 'text-success', 'text-primary')
    } catch (e) {
    }
}


greenPlant()