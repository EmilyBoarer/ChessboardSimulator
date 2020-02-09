import pygame
import time

#images copyright wikimedia commons user:Cburnett

# board is as shown

# h1,g1, f1 ... a1
# h2 ...        a2
# ...
# h8

#translates to 

# 0,0  1,0 .. 7,0
# .. 
# 0,7

class Tile(pygame.sprite.Sprite):
    def __init__(self, letter, number, boardmanager, tilewidth):
        super().__init__()
        self.letter = letter
        self.number = number
        self.x = "ABCDEFGH"[::-1].index(letter)
        self.y = int(number) - 1
        self.piece = None
        self.image = pygame.Surface((tilewidth, tilewidth))
        self.image.fill((100,100,100))
        if (self.y+self.x) % 2 == 0:
            self.image.fill((170,170,170))
        self.rect = self.image.get_rect()
        self.rect.y = self.y*tilewidth
        self.rect.x = self.x*tilewidth
        boardmanager.tilesprites.add(self)
    def textdata(self):
        return "HGFEDCBA"[self.x] + str(self.y+1)

class Button(pygame.sprite.Sprite):
    def __init__(self, boardmanager, screenx, screeny, width, height, text):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill((100,100,100))
        self.font = pygame.font.Font("fonts/OCRAEXT.TTF", height//2)
        h=0
        for part in text.split("@"):
            self.image.blit(self.font.render(part, 1, (0,0,0)),(0,h))
            h += height // 2 
        self.rect = self.image.get_rect()
        self.rect.y = screeny
        self.rect.x = screenx
        self.boardmanager = boardmanager
        boardmanager.buttonsprites.add(self)
    def onpixel(self, x, y):
        tx = self.rect.x
        ty = self.rect.y
        if tx < x and x < tx + self.width and ty < y and y < ty + self.height:
            return True
        return False
    def mousedown(self, mx, my):
        if self.onpixel(mx, my):
            self.press()
    def press(self):
        time.sleep(0.2)

class ClearButton(Button):
    def press(self):
        self.boardmanager.clear()
        super().press()

class NewgameButton(Button):
    def press(self):
        self.boardmanager.startnewgame()
        super().press()

class NewpieceButton(Button):
    def __init__(self, boardmanager, screenx, screeny, tilewidth, filepath):
        super().__init__(boardmanager, screenx, screeny, tilewidth, tilewidth, "")
        self.tilewidth = tilewidth
        self.image = pygame.transform.smoothscale(pygame.image.load(filepath), (self.tilewidth, self.tilewidth))

#there has got to be a better way to deal with all the buttons, but this still works fine it is just rather bulky

class NewBlackPawnButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackPawn.png")
    def press(self):
        self.boardmanager.add_game_piece(Pawn(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackCastleButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackCastle.png")
    def press(self):
        self.boardmanager.add_game_piece(Castle(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackKnightButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackKnight.png")
    def press(self):
        self.boardmanager.add_game_piece(Knight(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackBishopButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackBishop.png")
    def press(self):
        self.boardmanager.add_game_piece(Bishop(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackKingButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackKing.png")
    def press(self):
        self.boardmanager.add_game_piece(King(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackQueenButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackQueen.png")
    def press(self):
        self.boardmanager.add_game_piece(Queen(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackUnicornButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackUnicorn.png")
    def press(self):
        self.boardmanager.add_game_piece(Unicorn(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewBlackQueenMotherButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\BlackMann.png")
    def press(self):
        self.boardmanager.add_game_piece(QueenMother(False, self.boardmanager, self.tilewidth),"A",1)
        super().press()


class NewWhitePawnButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhitePawn.png")
    def press(self):
        self.boardmanager.add_game_piece(Pawn(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteCastleButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteCastle.png")
    def press(self):
        self.boardmanager.add_game_piece(Castle(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteKnightButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteKnight.png")
    def press(self):
        self.boardmanager.add_game_piece(Knight(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteBishopButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteBishop.png")
    def press(self):
        self.boardmanager.add_game_piece(Bishop(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteKingButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteKing.png")
    def press(self):
        self.boardmanager.add_game_piece(King(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteQueenButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteQueen.png")
    def press(self):
        self.boardmanager.add_game_piece(Queen(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteUnicornButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteUnicorn.png")
    def press(self):
        self.boardmanager.add_game_piece(Unicorn(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()

class NewWhiteQueenMotherButton(NewpieceButton):
    def __init__(self, boardmanager, screenx, screeny, tilewidth):
        super().__init__(boardmanager, screenx, screeny, tilewidth, "pngs\\WhiteMann.png")
    def press(self):
        self.boardmanager.add_game_piece(QueenMother(True, self.boardmanager, self.tilewidth),"A",1)
        super().press()


    
class Board:
    def __init__(self, tilewidth):
        self.pieces = []
        self.tilesprites = pygame.sprite.Group()
        self.piecesprites = pygame.sprite.Group()
        self.buttonsprites = pygame.sprite.Group()
        self.tiles = [[Tile(letter,number, self, tilewidth) for letter in "ABCDEFGH"[::-1]] for number in range(0,9)]
        self.tilewidth = tilewidth
        self.toppriority = pygame.sprite.Group()
        self.picked_up = None
        self.STRICTPLACEMENT = False
        self.buttons = []
    def clear(self):
        self.pieces = []
        self.tilesprites = pygame.sprite.Group()
        self.piecesprites = pygame.sprite.Group()
        self.tiles = [[Tile(letter,number, self, self.tilewidth) for letter in "ABCDEFGH"[::-1]] for number in range(0,9)]
        self.toppriority = pygame.sprite.Group()
        self.picked_up = None
    def startnewgame(self):
        self.clear()
        for l in "ABCDEFGH":
            self.add_game_piece(Pawn(True, self, self.tilewidth), l, 2)
            self.add_game_piece(Pawn(False, self, self.tilewidth), l, 7)
        self.add_game_piece(Castle(True, self, self.tilewidth), "A", 1)
        self.add_game_piece(Knight(True, self, self.tilewidth), "B", 1)
        self.add_game_piece(Bishop(True, self, self.tilewidth), "C", 1)
        self.add_game_piece(Queen(True, self, self.tilewidth), "D", 1)
        self.add_game_piece(King(True, self, self.tilewidth), "E", 1)
        self.add_game_piece(Bishop(True, self, self.tilewidth), "F", 1)
        self.add_game_piece(Knight(True, self, self.tilewidth), "G", 1)
        self.add_game_piece(Castle(True, self, self.tilewidth), "H", 1)

        self.add_game_piece(Castle(False, self, self.tilewidth), "A", 8)
        self.add_game_piece(Knight(False, self, self.tilewidth), "B", 8)
        self.add_game_piece(Bishop(False, self, self.tilewidth), "C", 8)
        self.add_game_piece(Queen(False, self, self.tilewidth), "D", 8)
        self.add_game_piece(King(False, self, self.tilewidth), "E", 8)
        self.add_game_piece(Bishop(False, self, self.tilewidth), "F", 8)
        self.add_game_piece(Knight(False, self, self.tilewidth), "G", 8)
        self.add_game_piece(Castle(False, self, self.tilewidth), "H", 8)
    def getstrictplacement(self):
        return self.STRICTPLACEMENT
    def add_game_piece(self, piece, x, y):
        self.pieces.append(piece)
        piece.set_tile(self.tiles[y]["ABCDEFGH"[::-1].index(x)])
    def add_button(self, button):
        self.buttons.append(button)
    def draw_demopieces(self, screen):
        for piece in self.pieces:
            piece.demopieces.draw(screen)
    def ispiece(self, x, y):
        for piece in self.pieces:
            if piece.tile.x == x and piece.tile.y == y:
                return True
        return False
    def piecewhite(self, x, y):
        for piece in self.pieces:
            if piece.tile.x == x and piece.tile.y == y:
                return piece.white
        return None
    def placefromdrag(self, piece):
        #check and declare vars
        x = (piece.dragx + piece.dragoffx) // self.tilewidth
        y = (piece.dragy + piece.dragoffy) // self.tilewidth

        if x > 7: 
            piece.setpostotile() # cannot be placed
            return

        #remove old state (not done by overriding in new setup)
        piece.tile.piece = None

        #set up new state
        piece.rect.x = x * self.tilewidth
        piece.rect.y = y * self.tilewidth
        
        tile = self.tiles[y+1][x]

        if tile.piece != None:
            tile.piece.take() # take piece, remove from game

        piece.tile = tile
        tile.piece = piece # gotta set both way refrencing
            
class DemoPlaceholder(pygame.sprite.Sprite):
    def __init__(self, x, y, col, parent):
        super().__init__()
        self.image = pygame.Surface((tilewidth/2, tilewidth/2))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = (x+0.25)*parent.tilewidth
        self.rect.y = (y+0.25)*parent.tilewidth
        parent.demopieces.add(self)
        
class Piece(pygame.sprite.Sprite):
    def __init__(self, name, white, boardmanager, tilewidth):
        super().__init__()
        self.name = name
        self.tile = None
        self.white = white # bool true if white false is black
        self.moves = [] ## IMPORTANT ## the moves muct be in lists that go in order where first is closest to piece
        self.tilewidth = tilewidth
        self.image = pygame.Surface((tilewidth, tilewidth))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.boardmanager = boardmanager
        self.boardmanager.piecesprites.add(self)
        self.demopieces = pygame.sprite.Group()
        self.dragx = None
        self.dragy = None
        self.dragoffx = 0
        self.dragoffy = 0
    def setpostotile(self):
        self.rect.y = self.tile.y*self.tilewidth
        self.rect.x = self.tile.x*self.tilewidth
    def getmoves(self): # returns list of lists of spurs that can be taken for moving
        return self.moves # this is here so can be overriden for pawns!
    def gettakemoves(self): # returns list of lists of spurs that can be taken for taking
        return self.moves
    def set_png(self, filepath):
        self.image = pygame.transform.smoothscale(pygame.image.load(filepath), (self.tilewidth, self.tilewidth))
    def set_tile(self, tile):
        self.tile = tile
        self.tile.piece = self
        self.rect.y = self.tile.y*self.tilewidth
        self.rect.x = self.tile.x*self.tilewidth
    def show_possibilities(self):
        x = self.tile.x
        y = self.tile.y
        for move_set in self.getmoves():
            for rel_pos in move_set:
                rx, ry = rel_pos
                if self.boardmanager.ispiece(x+rx, y+ry) or x+rx < 0 or y+ry < 0 or x+rx > 7 or y+ry > 7:
                    break
                DemoPlaceholder(x+rx, y+ry, (255,255,0), self)
        for move_set in self.gettakemoves():
            for rel_pos in move_set:
                rx, ry = rel_pos
                if self.boardmanager.ispiece(x+rx, y+ry):
                    if self.boardmanager.piecewhite(x+rx, y+ry) != self.white:
                        if not(x+rx < 0 or y+ry < 0 or x+rx > 7 or y+ry > 7): # check if in bounds to board
                            DemoPlaceholder(x+rx, y+ry, (255,0,0), self) # create red placeholder then stop after
                    break
    def possible(self, destx, desty):
        if not self.boardmanager.getstrictplacement(): return True # if there is free placement, allow anything
        x = self.tile.x
        y = self.tile.y
        for move_set in self.getmoves():
            for rel_pos in move_set:
                rx, ry = rel_pos
                if x+rx == destx and y+ry == desty:
                    if not self.boardmanager.ispiece(destx, desty):
                        if not (x+rx < 0 or y+ry < 0 or x+rx > 7 or y+ry > 7):
                            return True # nothing there
        for move_set in self.gettakemoves():
            for rel_pos in move_set:
                rx, ry = rel_pos
                if x+rx == destx and y+ry == desty:
                    if self.boardmanager.ispiece(destx, desty):
                        if self.boardmanager.piecewhite(destx, desty) != self.white:
                            if not(x+rx < 0 or y+ry < 0 or x+rx > 7 or y+ry > 7):
                                return True # can take that piece
        return False
    def hide_possibilities(self):
        self.demopieces.empty() # remove all demosprites (they will automatically be deleted from RAM) TODO check they actually are?
    def onpixel(self, x, y):
        tx = self.tile.x * self.tilewidth
        ty = self.tile.y * self.tilewidth
        if tx < x and x < tx + self.tilewidth and ty < y and y < ty + self.tilewidth:
            return True
        return False
    def startdrag(self, x, y):
        tx = self.tile.x * self.tilewidth
        ty = self.tile.y * self.tilewidth
        self.dragx = tx
        self.dragy = ty
        self.dragoffx = x - tx
        self.dragoffy = y - ty
    def dragto(self, x, y):
        self.dragx = x - self.dragoffx
        self.dragy = y - self.dragoffy
        self.rect.x = self.dragx
        self.rect.y = self.dragy
    def place(self):
        self.boardmanager.placefromdrag(self)
    def abandondrag(self):
        self.rect.x = self.tile.x * self.tilewidth
        self.rect.y = self.tile.y * self.tilewidth
    def dragpossible(self):
        x = (self.dragx + self.dragoffx) // self.tilewidth
        y = (self.dragy + self.dragoffy) // self.tilewidth
        return self.possible(x,y)
    def take(self):
        self.boardmanager.pieces.remove(self)
        self.boardmanager.piecesprites.remove(self)
        self.kill()

class Pawn(Piece):
    def __init__(self,  white, boardmanager, tilewidth):
        super().__init__("Pawn", white, boardmanager, tilewidth)
        if self.white:
            self.set_png("pngs\\WhitePawn.png")
        else:
            self.set_png("pngs\\BlackPawn.png")
    def getmoves(self):
        if self.white:
            if self.tile.y == 1:
                return [[(0,1),(0,2)]]
            return [[(0,1)]]
        else:
            if self.tile.y == 6:
                return [[(0,-1),(0,-2)]]
            return [[(0,-1)]]
    def gettakemoves(self):
        if self.white:
            return [[(1,1)],[(-1,1)]]
        else:
            return [[(1,-1)],[(-1,-1)]]        

class Castle(Piece):
    def __init__(self, white, boardmanager, tilewidth):
        super().__init__("Castle", white, boardmanager, tilewidth)
        self.moves = [
            [(0,x) for x in [1,2,3,4,5,6,7,8]],
            [(0,x) for x in [-1,-2,-3,-4,-5,-6,-7,-8]],
            [(x,0) for x in [1,2,3,4,5,6,7,8]],
            [(x,0) for x in [-1,-2,-3,-4,-5,-6,-7,-8]]
            ]
        if self.white:
            self.set_png("pngs\\WhiteCastle.png")
        else:
            self.set_png("pngs\\BlackCastle.png")

class Bishop(Piece):
    def __init__(self, white, boardmanager, tilewidth):
        super().__init__("Bishop", white, boardmanager, tilewidth)
        self.moves = [
            [( c, c) for c in [1,2,3,4,5,6,7,8]],
            [(-c, c) for c in [1,2,3,4,5,6,7,8]],
            [( c,-c) for c in [1,2,3,4,5,6,7,8]],
            [(-c,-c) for c in [1,2,3,4,5,6,7,8]]
            ]
        if self.white:
            self.set_png("pngs\\WhiteBishop.png")
        else:
            self.set_png("pngs\\BlackBishop.png")

class Knight(Piece):
    def __init__(self, white, boardmanager, tilewidth):
        super().__init__("Knight", white, boardmanager, tilewidth)
        self.moves = [
            [(1,2)],
            [(-1,2)],
            [(1,-2)],
            [(-1,-2)],
            [(2,1)],
            [(2,-1)],
            [(-2,1)],
            [(-2,-1)],
            ]
        if self.white:
            self.set_png("pngs\\WhiteKnight.png")
        else:
            self.set_png("pngs\\BlackKnight.png")

class Queen(Piece):
    def __init__(self,  white, boardmanager, tilewidth):
        super().__init__("Queen", white, boardmanager, tilewidth)
        self.moves = [
            [( c, c) for c in [1,2,3,4,5,6,7,8]],
            [(-c, c) for c in [1,2,3,4,5,6,7,8]],
            [( c,-c) for c in [1,2,3,4,5,6,7,8]],
            [(-c,-c) for c in [1,2,3,4,5,6,7,8]],
            [(0,x) for x in [1,2,3,4,5,6,7,8]],
            [(0,x) for x in [-1,-2,-3,-4,-5,-6,-7,-8]],
            [(x,0) for x in [1,2,3,4,5,6,7,8]],
            [(x,0) for x in [-1,-2,-3,-4,-5,-6,-7,-8]]
            ]
        if self.white:
            self.set_png("pngs\\WhiteQueen.png")
        else:
            self.set_png("pngs\\BlackQueen.png")

class King(Piece):
    def __init__(self,  white, boardmanager, tilewidth):
        super().__init__("King", white, boardmanager, tilewidth)
        self.moves = [
            [(0,1)],
            [(0,-1)],
            [(1,0)],
            [(-1,0)],
            [(1,1)],
            [(1,-1)],
            [(-1,1)],
            [(-1,-1)]
        ]
        if self.white:
            self.set_png("pngs\\WhiteKing.png")
        else:
            self.set_png("pngs\\BlackKing.png")

#custom piecesclass 
class Unicorn(Piece):
    def __init__(self, white, boardmanager, tilewidth):
        super().__init__("Unicorn", white, boardmanager, tilewidth)
        self.moves = [
            [(1,2)],
            [(-1,2)],
            [(1,-2)],
            [(-1,-2)],
            [(2,1)],
            [(2,-1)],
            [(-2,1)],
            [(-2,-1)],
            [(2,0)],
            [(-2,0)],
            [(0,2)],
            [(0,-2)],
            # [(3,2)],
            # [(-3,2)],
            # [(3,-2)],
            # [(-3,-2)],
            # [(2,3)],
            # [(2,-3)],
            # [(-2,3)],
            # [(-2,-3)],
            ]
        if self.white:
            self.set_png("pngs\\WhiteUnicorn.png")
        else:
            self.set_png("pngs\\BlackUnicorn.png")

class QueenMother(Piece):
    def __init__(self,  white, boardmanager, tilewidth):
        super().__init__("Queen", white, boardmanager, tilewidth)
        self.moves = [
            [( c, c) for c in [1,2,3,4,5,6,7,8]],
            [(-c, c) for c in [1,2,3,4,5,6,7,8]],
            [( c,-c) for c in [1,2,3,4,5,6,7,8]],
            [(-c,-c) for c in [1,2,3,4,5,6,7,8]],
            [(0,x) for x in [1,2,3,4,5,6,7,8]],
            [(0,x) for x in [-1,-2,-3,-4,-5,-6,-7,-8]],
            [(x,0) for x in [1,2,3,4,5,6,7,8]],
            [(x,0) for x in [-1,-2,-3,-4,-5,-6,-7,-8]],
            [( c, 2*c) for c in [1,2,3,4,5,6,7,8]],
            [( c, -2*c) for c in [1,2,3,4,5,6,7,8]],
            [(-c, 2*c) for c in [1,2,3,4,5,6,7,8]],
            [(-c, -2*c) for c in [1,2,3,4,5,6,7,8]],
            [(2*c, c) for c in [1,2,3,4,5,6,7,8]],
            [(-2*c, c) for c in [1,2,3,4,5,6,7,8]],
            [(2*c, -c) for c in [1,2,3,4,5,6,7,8]],
            [(-2*c, -c) for c in [1,2,3,4,5,6,7,8]],
            ]
        if self.white:
            self.set_png("pngs\\WhiteMann.png")
        else:
            self.set_png("pngs\\BlackMann.png")




tilewidth = 100
width, height = tilewidth*8, tilewidth*8

pygame.init()
screen = pygame.display.set_mode((width+tilewidth*4,height))
pygame.display.set_caption("Chessboard Simulator")

board = Board(tilewidth)

board.add_button(ClearButton(board, tilewidth*9, 0, tilewidth*2, tilewidth, "Clear"))
board.add_button(NewgameButton(board, tilewidth*9, tilewidth, tilewidth*2, tilewidth, "New@Game"))

board.add_button(NewBlackPawnButton(board, tilewidth*9, tilewidth*2, tilewidth))
board.add_button(NewBlackCastleButton(board, tilewidth*9, tilewidth*3, tilewidth))
board.add_button(NewBlackKnightButton(board, tilewidth*9, tilewidth*4, tilewidth))
board.add_button(NewBlackBishopButton(board, tilewidth*9, tilewidth*5, tilewidth))
board.add_button(NewBlackKingButton(board, tilewidth*9, tilewidth*6, tilewidth))
board.add_button(NewBlackQueenButton(board, tilewidth*9, tilewidth*7, tilewidth))

board.add_button(NewWhitePawnButton(board, tilewidth*10, tilewidth*2, tilewidth))
board.add_button(NewWhiteCastleButton(board, tilewidth*10, tilewidth*3, tilewidth))
board.add_button(NewWhiteKnightButton(board, tilewidth*10, tilewidth*4, tilewidth))
board.add_button(NewWhiteBishopButton(board, tilewidth*10, tilewidth*5, tilewidth))
board.add_button(NewWhiteKingButton(board, tilewidth*10, tilewidth*6, tilewidth))
board.add_button(NewWhiteQueenButton(board, tilewidth*10, tilewidth*7, tilewidth))

board.add_button(NewWhiteUnicornButton(board, tilewidth*11, tilewidth*4, tilewidth))
board.add_button(NewWhiteQueenMotherButton(board, tilewidth*11, tilewidth*5, tilewidth))
board.add_button(NewBlackUnicornButton(board, tilewidth*11, tilewidth*6, tilewidth))
board.add_button(NewBlackQueenMotherButton(board, tilewidth*11, tilewidth*7, tilewidth))


board.startnewgame()

clock = pygame.time.Clock()


RUNNING = True
while RUNNING:
    ticks = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        RUNNING = False

    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        #start dragging piece if needed
        if board.picked_up == None:
            for p in board.pieces:
                if p.onpixel(mx, my):
                    board.picked_up = p
                    board.picked_up.show_possibilities()
                    board.picked_up.startdrag(mx, my)
                    board.toppriority.add(board.picked_up)
        else:
            board.picked_up.dragto(mx, my)
        if board.picked_up == None:
            #check all buttons for presses
            for button in board.buttons:
                button.mousedown(mx, my)
    
    elif board.picked_up != None: # drop the piece on the board (back where is was if not able to be placed)
        if board.picked_up.dragpossible():
            board.picked_up.place()
        else:
            board.picked_up.abandondrag()
        board.picked_up.hide_possibilities()
        board.picked_up = None
        board.toppriority.empty()
        

    
    screen.fill((200,200,200))
    board.tilesprites.draw(screen)
    board.piecesprites.draw(screen)
    board.buttonsprites.draw(screen)
    board.draw_demopieces(screen)
    board.toppriority.draw(screen)
    pygame.display.flip()

pygame.quit()
    









