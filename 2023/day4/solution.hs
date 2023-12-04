import qualified Data.Set as S

intWordsToInts :: String -> [Int]
intWordsToInts s = map (\num -> read num :: Int) $ words s

main = do
    contents <- getContents
    let ls = lines contents
        justNums = map (drop 2 . dropWhile (/=':')) ls
        winningAndOwn = [ [intWordsToInts $ takeWhile (/='|') x] ++ [intWordsToInts $ tail $ dropWhile (/='|') x] | x <- justNums ]
        commonNums = map (\[xs, ys] -> (S.fromList xs) `S.intersection` (S.fromList ys)) winningAndOwn
        points = map ((^) 2 . (-1+) . length) (filter ((>0) . length) commonNums)
    print $ sum points