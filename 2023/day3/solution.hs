import Data.Char (isDigit)

inBounds :: Int -> Int -> Int -> Int -> Bool
inBounds r c ri ci = (ri >= 0 && ri < r) && (ci >= 0 && ci < c)

-- Extract a number from a string starting at position ci. Return the part left of ci and part right of ci as a tuple of strings
extractNumStr :: [Char] -> Int -> (String, String)
extractNumStr s ci = (digitsLeft, digitsRight)
    where
        digitsLeft = reverse $ takeWhile isDigit (reverse $ take ci s)
        digitsRight = takeWhile isDigit (drop ci s)

-- Check that a character is not a digit or a dot
isSpecialSymbol :: [[Char]] -> Int -> Int -> Int -> Int -> Bool 
isSpecialSymbol m r c ri ci
    | inBounds r c ri ci = (((m !! ri) !! ci) /= '.') && ((not . isDigit) ((m !! ri) !! ci))
    | otherwise = False


-- Starting from position (ri, ci) in the character matrix m, check positions [ci, endc] for integer numbers and return them in a list of strings
-- advance from left to right
checkDirection :: [[Char]] -> Int -> Int -> Int -> Int -> Int -> [String]
checkDirection m r c endc ri ci
    | ci >= endc = []
    | otherwise = case (if (inBounds r c ri ci) && (isDigit (m!!ri!!ci)) then Just(extractNumStr (m!!ri) ci) else Nothing) of 
        Just (left, right) -> (left ++ right):(checkDirection m r c endc ri (ci + (length right)))
        Nothing            -> checkDirection m r c endc ri (ci+1)


-- Collect adjacent integers around the position (ri, ci) from the character matrix m and return them in a list of strings
getAdjacentNums :: [[Char]] -> Int -> Int -> Int -> Int -> [String]
getAdjacentNums m r c ri ci = numsUp ++ numsDown ++ numsLeft ++ numsRight
    where
        numsUp    = checkDirection m r c (ci+2) (ri-1) (ci-1) 
        numsDown  = checkDirection m r c (ci+2) (ri+1) (ci-1) 
        numsLeft  = checkDirection m r c ci ri (ci-1) 
        numsRight = checkDirection m r c (ci+2) ri (ci+1) 

-- Find each special symbol from the character matrix m and return a list of list of strings where the first coordinate of each list of strings is the special symbol
-- and the other coordinates are the string representations of integers adjacent to the symbol
findSymbolAdjacentNums :: [[Char]] -> Int -> Int -> Int -> Int -> [[String]]
findSymbolAdjacentNums m r c ri ci
    | ri == r = []
    | ci == c = findSymbolAdjacentNums m r c (ri+1) 0
    | ((not . isDigit) sym) && (sym /= '.') = [[sym]:(getAdjacentNums m r c ri ci)] ++ (findSymbolAdjacentNums m r c ri (ci + 1))
    | otherwise = findSymbolAdjacentNums m r c ri (ci+1)
    where
        sym = (m !! ri) !! ci

main = do
    contents <- getContents
    let ls = lines contents
        nrow = length ls
        ncol = length (head ls)
        nums = findSymbolAdjacentNums ls nrow ncol 0 0
        sumOfInts = sum $ map (\xs -> foldl (+) 0 [read x :: Int | x <- xs]) $ map tail nums
        gearRatios = sum $ map (\xs -> foldl (*) 1 [read x :: Int | x <- xs]) $ [tail xs | xs <- nums, head xs == "*" && length xs == 3]
    print sumOfInts -- part 1
    print gearRatios -- part 2
