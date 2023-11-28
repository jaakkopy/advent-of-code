import Data.List (sortBy, groupBy)

groupByNonEmpty :: [[a]] -> [[[a]]]
groupByNonEmpty = groupBy (\x y -> not (null x) && not (null y))

dropEmpty :: [[[a]]] -> [[[a]]]
dropEmpty = filter (not . any null)

convertToInts :: [[String]] -> [[Int]]
convertToInts = map (map (\ x -> read x :: Int))

countSums :: [[Int]] -> [Int]
countSums = map sum

sortReversed :: [Int] -> [Int]
sortReversed = sortBy (flip compare)

main = do
    contents <- getContents 
    let groups = sortReversed $ countSums $ convertToInts $ dropEmpty $ groupByNonEmpty $ lines contents
    -- Part 1
    print $ head groups
    -- Part 2
    print $ sum $ take 3 groups