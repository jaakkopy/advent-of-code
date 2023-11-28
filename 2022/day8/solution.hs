import Data.Char (digitToInt)

-- returns (is visible from one of the edges (boolean), how many trees are visible from the starting point (integer))
isGreater :: (Ord t1, Num t2) => t1 -> Int -> Int -> Int -> Int -> [[t1]] -> Int -> Int -> t2 -> (Bool, t2)
isGreater startVal r c rdir cdir grid rows cols viewCount
    | r == rows || r == -1 || c == cols || c == -1 = (True, viewCount)
    | ((grid !! r) !! c) >= startVal = (False, viewCount + 1)
    | otherwise = isGreater startVal (r + rdir) (c + cdir) rdir cdir grid rows cols (viewCount + 1)

-- returns (visible trees (integer), highest scenic score (integer))
countVisible :: (Num a1, Ord a2, Ord b, Num b) => [[a2]] -> Int -> Int -> (a1, b) -> (a1, b)
countVisible g r c (seen, scenicScore)
    | r == rows = (seen, scenicScore)
    | otherwise = if isVisible then countVisible g nextRow nextCol (seen + 1, newScore) else countVisible g nextRow nextCol (seen, newScore)
    where rows = length g
          cols = length (head g)
          nextCol = if c == cols - 1 then 0 else c + 1
          nextRow = if nextCol > c   then r else r + 1
          startVal = (g !! r) !! c
          (gd, sd) = isGreater startVal (r+1) c   1   0  g rows cols 0
          (gu, su) = isGreater startVal (r-1) c (-1)  0  g rows cols 0
          (gl, sl) = isGreater startVal r (c+1)   0   1  g rows cols 0
          (gr, sr) = isGreater startVal r (c-1)   0 (-1) g rows cols 0
          isVisible = gd || gu || gl || gr
          newScore = max (sd * su * sl * sr) scenicScore

main :: IO ()
main = do
    contents <- getContents
    let grid =  map (map digitToInt) $ lines contents
    print $ countVisible grid 0 0 (0, 0)
