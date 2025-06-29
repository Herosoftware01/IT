document.addEventListener('DOMContentLoaded', function () {
    let currentCell = null;
    const scrollContainer = document.querySelector('#scroll-container') || document.querySelector('.results');

    document.querySelectorAll('.results table td').forEach(td => {
        td.style.cursor = 'pointer';
        td.addEventListener('click', () => {
            if (currentCell) currentCell.classList.remove('selected-cell');
            td.classList.add('selected-cell');
            currentCell = td;
            scrollCellIntoView(td);
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
            scrollCellIntoView(nextCell);
        }
    });

    function scrollCellIntoView(cell) {
        if (!scrollContainer || !cell) return;

        const cellRect = cell.getBoundingClientRect();
        const containerRect = scrollContainer.getBoundingClientRect();

        if (cellRect.top < containerRect.top) {
            scrollContainer.scrollTop -= (containerRect.top - cellRect.top + 10);
        } else if (cellRect.bottom > containerRect.bottom) {
            scrollContainer.scrollTop += (cellRect.bottom - containerRect.bottom + 10);
        }
    }
});
