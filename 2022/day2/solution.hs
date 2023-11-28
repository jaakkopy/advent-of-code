import Data.Char
import qualified Data.Map as Map

followGuide (m:moves) score guide
    | null moves = nextScore 
    | otherwise = followGuide moves nextScore guide
    where nextScore = (+score) $ (guide Map.! head m) Map.! (m !! 1)
followGuide [] _ _ = 0

main = do
    contents <- getContents
    let moves = map words $ lines contents
        -- Scores: rock = 1, paper = 2, scissors = 3
        a1 = Map.fromList [("X", 1+3), ("Y", 2+6), ("Z", 3+0)] -- rock
        b1 = Map.fromList [("X", 1+0), ("Y", 2+3), ("Z", 3+6)] -- paper
        c1 = Map.fromList [("X", 1+6), ("Y", 2+0), ("Z", 3+3)] -- scissors
        guide1 = Map.fromList [("A", a1), ("B", b1), ("C", c1)]
        a2 = Map.fromList [("X", 3+0), ("Y", 1+3), ("Z", 2+6)] -- rock:     lose scissors, draw rock,     win paper
        b2 = Map.fromList [("X", 1+0), ("Y", 2+3), ("Z", 3+6)] -- paper:    lose rock,     draw paper,    win scissors
        c2 = Map.fromList [("X", 2+0), ("Y", 3+3), ("Z", 1+6)] -- scissors: lose paper,    draw scissors, win rock
        guide2 = Map.fromList [("A", a2), ("B", b2), ("C", c2)]
    -- part 1
    print $ followGuide moves 0 guide1
    -- part 2
    print $ followGuide moves 0 guide2