
makeSequences :: [Int] -> [[Int]]
makeSequences history
    | all (==0) history = [history]
    | otherwise = history : makeSequences next
    where next = zipWith (-) (tail history) history

extrapolateWith :: Num a => (b -> c) -> (c -> a -> a) -> [b] -> a
extrapolateWith pickFrom combineWith (s:sequences)
    | null sequences = 0
    | otherwise = (pickFrom s) `combineWith` (extrapolateWith pickFrom combineWith sequences)

main = do
    contents <- getContents
    let histories = map (\x -> map (\y -> read y :: Int) x) $ map words $ lines contents
    print $ sum $ map ( (extrapolateWith last (+)) . makeSequences) histories -- part 1
    print $ sum $ map ( (extrapolateWith head (-)) . makeSequences) histories -- part 2
