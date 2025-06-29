document.addEventListener('DOMContentLoaded', function () {
    let currentCell = null;

    document.querySelectorAll('td').forEach(td => {
        td.style.cursor = 'pointer';
        td.addEventListener('click', () => {
            if (currentCell) {
                currentCell.classList.remove('selected-cell');
            }
            td.classList.add('selected-cell');
            currentCell = td;
            scrollToCell(td);
        });
    });

    document.addEventListener('keydown', function (e) {
        if (!currentCell) return;

        const td = currentCell;
        const tr = td.parentElement;
        const cellIndex = Array.from(tr.children).indexOf(td);
        let nextCell = null;

        if (e.key === 'ArrowRight') {
            nextCell = td.nextElementSibling;
        } else if (e.key === 'ArrowLeft') {
            nextCell = td.previousElementSibling;
        } else if (e.key === 'ArrowDown') {
            const nextRow = tr.nextElementSibling;
            if (nextRow) nextCell = nextRow.children[cellIndex];
        } else if (e.key === 'ArrowUp') {
            const prevRow = tr.previousElementSibling;
            if (prevRow) nextCell = prevRow.children[cellIndex];
        }

        if (nextCell) {
            currentCell.classList.remove('selected-cell');
            nextCell.classList.add('selected-cell');
            currentCell = nextCell;
            scrollToCell(nextCell);
        }
    });

    function scrollToCell(cell) {
        // Scroll only if out of view
        const rect = cell.getBoundingClientRect();
        const buffer = 40;  // add padding

        const isAbove = rect.top < buffer;
        const isBelow = rect.bottom > window.innerHeight - buffer;
        const isLeft = rect.left < buffer;
        const isRight = rect.right > window.innerWidth - buffer;

        if (isAbove || isBelow || isLeft || isRight) {
            cell.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
        }
    }
});
