import qualified Data.Set as S

intWordsToInts :: String -> [Int]
intWordsToInts s = map (\num -> read num :: Int) $ words s

commonNums = \[xs, ys] -> S.toList $ (S.fromList xs) `S.intersection` (S.fromList ys)

countPointsForCommonNums xs = if l > 0 then ((^) 2 . (-1+) . length) xs else 0
    where l = length xs

-- Part 2 is a dynamic programming problem. This uses a memo to store previously computed values
part2 :: [Int] -> Int
part2 amountCommonNums = sum $ map (memo !!) [0..(n-1)]
    where
        memo = map part2' [0..n]
        part2' i
            | i >= n = 0 
            | otherwise = 1 + copies
            where
                cs = (amountCommonNums !! i)
                copies = sum $ map (memo !!) [(i+1)..(i+cs)]
        n = length amountCommonNums


main = do
    contents <- getContents
    let ls = lines contents
        justNums = map (drop 2 . dropWhile (/=':')) ls
        cards = [ [intWordsToInts $ takeWhile (/='|') x] ++ [intWordsToInts $ tail $ dropWhile (/='|') x] | x <- justNums ]
        cNums = map commonNums cards
        p1 = map countPointsForCommonNums $ cNums
    print $ sum p1 -- part 1
    print $ part2 $ map length cNums -- part 2