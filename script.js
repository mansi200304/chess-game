document.addEventListener("DOMContentLoaded", () => {
    const boardElement = document.getElementById("board");

    // Fetch initial board state
    fetch('/api/board')
        .then(response => response.json())
        .then(board => {
            renderBoard(board);
        });

    function renderBoard(board) {
        boardElement.innerHTML = '';
        board.forEach((row, i) => {
            row.forEach((piece, j) => {
                const square = document.createElement("div");
                square.className = "square " + ((i + j) % 2 === 0 ? "white" : "black");
                square.textContent = piece === '.' ? '' : piece;
                square.addEventListener('click', () => handleSquareClick(i, j));
                boardElement.appendChild(square);
            });
        });
    }

    function handleSquareClick(row, col) {
        // Handle piece movement logic here
        console.log(`Clicked on square at ${row}, ${col}`);
        // You can implement move logic and call /api/move endpoint here.
    }
});
