checkRanges :: [a] -> (a -> Bool) -> Int
checkRanges ranges pred = checkRanges' ranges
    where checkRanges' (x:xs)
            | null xs   = if pred x then 1 else 0
            | otherwise = if pred x then 1 + checkRanges' xs else checkRanges' xs
          checkRanges' [] = 0

splitBy :: Eq a => a -> [a] -> [[a]]
splitBy delim x = [firstPart, secondPart]
    where firstPart  = takeWhile (/= delim) x
          secondPart = drop (length firstPart + 1) x

extractRange :: [Char] -> [[Int]]
extractRange r =  map (map (\x -> read x :: Int) . splitBy '-') $ splitBy ',' r

fullyContains :: Ord a => [[a]] -> Bool
fullyContains rs = fullyContains' r1 r2 || fullyContains' r2 r1
    where 
        [r1, r2] = rs
        fullyContains' a b = (a !! 0) <= (b !! 0) && (a !! 1) >= (b !! 1)

overlaps rs = overlaps' r1 r2 || overlaps' r2 r1
    where [r1, r2] = rs
          overlaps' a b = ((a !! 0) >= (b !! 0) && (a !! 1) <= (b !! 1)) || ((b !! 0) >= (a !! 0) && (b !! 0) <= (a !! 1))

main = do
    contents <- getContents
    let ranges = map extractRange $ lines contents
    -- Part 1
    print $ checkRanges ranges fullyContains 
    -- Part 2
    print $ checkRanges ranges overlaps