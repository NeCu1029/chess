import chess
import pos


def base(board: chess.BaseBoard) -> int:
    res = 0
    bs = str(board).split()
    for i in range(64):
        if bs[i] in pos.score:
            res += pos.score[bs[i]][i]
        elif bs[i].upper() in pos.score:
            r, c = divmod(i, 8)
            j = 8 * (7 - r) + c
            res -= pos.score[bs[i].upper()][j]
    return res


def val(
    board: chess.Board, alpha: int = -1000000, beta: int = 1000000, depth: int = 3
) -> int:
    if depth == 0:
        return (base(board), None)
    if board.is_stalemate():
        return (30 * (1 - 2 * board.turn), None)

    res = 1000000 * (1 - 2 * board.turn)
    rmove = None
    check = []
    capture = []
    nothing = []
    for move in board.legal_moves:
        board.push(move)
        if board.is_check():
            check.append(move)
            board.pop()
            continue
        board.pop()
        if board.is_capture(move):
            capture.append(move)
        else:
            nothing.append(move)

    for move in check + capture + nothing:
        iscapture = board.is_capture(move)
        board.push(move)
        if board.is_stalemate():
            cur = -30 * (1 - 2 * board.turn)
        elif board.is_checkmate():
            cur = 500000 * (1 - 2 * board.turn)
        elif depth == 1 and iscapture:
            cur = val(board, alpha, beta, 1)[0]
        else:
            cur = val(board, alpha, beta, depth - 1)[0]
        board.pop()

        if board.turn:
            if cur > res:
                res = cur
                rmove = move
            alpha = max(alpha, cur)
        else:
            if cur < res:
                res = cur
                rmove = move
            beta = min(beta, cur)
        if alpha >= beta:
            break

    return (res, rmove)


def move(board: chess.Board) -> chess.Move:
    return val(board)[1]


if __name__ == "__main__":
    board = chess.Board("rnb1kb1r/p6p/2p1p1p1/5p1B/Np1P4/7q/PPP2P1P/R1BQK2R")
    print(val(board))
    m = move(board)
    print(m)
    board.push(m)
    print(val(board))
