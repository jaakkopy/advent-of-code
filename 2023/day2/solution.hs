import Data.Char (isDigit, isSpace)
import Data.List (isPrefixOf)

limits = [12, 13, 14] -- Red = 0, Green = 1, Blue = 2

parseCube :: String -> [Int]
parseCube x = cubeList 
    where
        digitText = takeWhile (isDigit) (dropWhile isSpace x)
        amountCubes = read digitText :: Int
        colorText = dropWhile isSpace $ drop (length digitText + 1) x
        cubeList = 
            if isPrefixOf "red" colorText then [amountCubes, 0, 0]
            else if isPrefixOf "green" colorText then [0, amountCubes, 0]
            else [0, 0, amountCubes]


parseRound :: String -> [Int]
parseRound x
    | null x = [0, 0, 0]
    | otherwise = zipWith (+) cubes (parseRound (drop (length cubeText + 1) x))
    where 
        cubeText = takeWhile (/=',') x
        cubes = parseCube cubeText

parseGame :: String -> [[Int]]
parseGame x = parseGame' (drop 2 (dropWhile (/=':') x))
    where parseGame' xs
            | null xs = []
            | otherwise = (parseRound round):parseGame' (drop (length round + 1) xs)
            where round = takeWhile (/=';') xs

readGames :: [String] -> [[[Int]]] -- games, game, rounds (list of lists of lists)
readGames (x:xs)
    | null xs = [parseGame x]
    | otherwise = (parseGame x):(readGames xs)

countPossible :: [[[Int]]] -> Int -> Int
countPossible xs i
    | null xs = 0
    | otherwise = (if all (==True) [verify x | x <- head xs] then i else 0) + countPossible (tail xs) (i+1)
    where 
        verify round = all (==True) $ zipWith (<=) round limits

cubePowerSum :: [[[Int]]] -> Int
cubePowerSum xs
    | null xs = 0
    | otherwise = (maxR * maxG * maxB) + cubePowerSum (tail xs)
    where
        h = head xs
        maxR = maximum [(x !! 0) | x <- h]
        maxG = maximum [(x !! 1) | x <- h]
        maxB = maximum [(x !! 2) | x <- h]

main = do
    contents <- getContents
    let ls = lines contents
        games = readGames ls
    print $ countPossible games 1 -- part 1
    print $ cubePowerSum games     -- part 2