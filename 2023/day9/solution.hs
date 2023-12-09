

makeSequences :: [Int] -> [[Int]]
makeSequences history
    | all (==0) history = [history]
    | otherwise = history : makeSequences next
    where next = zipWith (-) (tail history) history

extrapolate :: [[Int]] -> Int
extrapolate (s:sequences)
    | null sequences = 0
    | otherwise = (last s) + (extrapolate sequences)

main = do
    contents <- getContents
    let histories = map (\x -> map (\y -> read y :: Int) x) $ map words $ lines contents
    print $ sum $ map (extrapolate . makeSequences) histories
