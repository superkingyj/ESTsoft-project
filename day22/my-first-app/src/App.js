import React, { useState } from 'react';
import './App.css';

const caculateWinner = (squares) => {
	let lines = [];

	// 가로 검사
	for(let i=0; i<25; i+=5){
		lines.push([i, i+1, i+2]);
		lines.push([i+1, i+2, i+3]);
		lines.push([i+2, i+3, i+4]);
	}

	// 세로 검사
	for(let i=0; i<5; i++){
		lines.push([i, i+5, i+10]);
		lines.push([i+5, i+10, i+15]);
		lines.push([i+10, i+15, i+20]);
	}

	lines.push([0, 6, 12], [5, 11, 17], [10, 16, 22]);
	lines.push([2, 6, 10], [7, 11, 15], [12, 16, 20]);

	for (let i=0; i<lines.length; i++){
		const [a, b, c] = lines[i];
		if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]){
			return squares[a];
		}
	}

	return squares.every(square => square != null) ? 'Tie' : null;
};

const Square = ({ value, onClick}) => (
	<button className="square" onClick={onClick}>{value}</button>
);

const Board = ({ squares, onClick}) => {
	const renderSquare = (i) => (
		<Square 
		 value={squares[i]}
		 onClick={() => onClick(i)}
		 />
	);

  return (
    <div>
      {[...Array(5)].map((_, i) => (  
        <div className='board-row' key={i}>
          {[...Array(5)].map((_, j) => renderSquare(i * 5 + j))}
        </div>
      ))}
    </div>
  );
};

const Game = () => {
	const [history, setHistory] = useState([Array(25).fill(null)]);
	const [xIsNext, setXIsNext] = useState(true);
	const winner = caculateWinner(history[history.length - 1]);
	const xO = xIsNext ? 'X' : 'O';

	const handleClick = (i) => {
		const squares = [...history[history.length - 1]];
		if (winner || squares[i]) return;
		squares[i] = xO;
		setHistory([...history, squares]);
		setXIsNext(!xIsNext);
	};

	const resetGame = () => {
		setHistory([Array(25).fill(null)]);
		setXIsNext(true);
	}

	return (
		<div className="game">
			<div className="game-board">
				<Board
					squares={history[history.length - 1]}
					onClick={(i) => handleClick(i)}
				/>
			</div>
			<div className="game-info">
				<div>{winner ? `Winner: ${winner}` : `Next Player: ${xO}`}</div>
				<button onClick={resetGame}>Reset Game</button>
			</div>
		</div>
	)
}

export default Game;

