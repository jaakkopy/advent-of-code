import Data.Char (isDigit)

directions = [(1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1)]

inBounds :: Int -> Int -> Int -> Int -> Bool
inBounds r c ri ci = (ri >= 0 && ri < r) && (ci >= 0 && ci < c)

extractNumStr :: [Char] -> Int -> Int -> (String, String)
extractNumStr s ri ci = (digitsLeft, digitsRight)
    where
        digitsLeft = reverse $ takeWhile isDigit (reverse $ take ci s)
        digitsRight = takeWhile isDigit (drop ci s)

isSpecialSymbol :: [[Char]] -> Int -> Int -> Int -> Int -> Bool 
isSpecialSymbol m r c ri ci
    | inBounds r c ri ci = (((m !! ri) !! ci) /= '.') && ((not . isDigit) ((m !! ri) !! ci))
    | otherwise = False

checkAdjacent :: [[Char]] -> Int -> Int -> Int -> Int -> Bool
checkAdjacent m r c ri ci = if (inBounds r c ri ci) && (isDigit ((m !! ri) !! ci)) 
    then if foldl (\acc (y,x) -> acc || (isSpecialSymbol m r c (ri+y) (ci+x))) False directions 
        then Just(extractNumStr (m !! ri) ri ci)
        else Nothing
    else Nothing

findSymbolAdjacentNums :: [[Char]] -> Int -> Int -> Int -> Int -> [Int]
findSymbolAdjacentNums m r c ri ci
    | ri == r = []
    | ci >= c = findSymbolAdjacentNums m r c (ri+1) 0
    | otherwise = case (checkAdjacent m r c ri ci) of 
        Just (left, right) -> (read (left ++ right) :: Int):(findSymbolAdjacentNums m r c ri (ci + (length right)))
        Nothing -> findSymbolAdjacentNums m r c ri (ci + 1)

main = do
    contents <- getContents
    let ls = lines contents
        nrow = length ls
        ncol = length (head ls)
    print $ sum $ findSymbolAdjacentNums ls nrow ncol 0 0