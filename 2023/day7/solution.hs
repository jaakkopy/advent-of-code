import qualified Data.Map as M
import Data.List
import Data.Ord

compareCards :: Char -> Char -> M.Map Char Int -> Ordering
compareCards c1 c2 orderMap = compare (orderMap M.! c1) (orderMap M.! c2)

countSameCards :: String -> [Int]
countSameCards h = reverse $ sort $ map length $ group $ sort h

replaceJs :: String -> String
replaceJs hand = map (\c -> if c == 'J' then most else c) hand
    where
        removedJs = filter (/='J') hand
        most = if (not . null) removedJs then (head . maximumBy (comparing length) . group . sort $ filter (/='J') hand) else 'J'

compareRanks :: String -> String -> Bool -> Ordering
compareRanks hand1 hand2 shouldReplaceJs = compare (countSameCards h1) (countSameCards h2)
    where h1 = if shouldReplaceJs then replaceJs hand1 else hand1
          h2 = if shouldReplaceJs then replaceJs hand2 else hand2

compareHands :: String -> String -> M.Map Char Int -> Bool -> Ordering
compareHands hand1 hand2 cardMap shouldReplaceJs = if rankComparison == EQ then compareHands' hand1 hand2 else rankComparison
    where
        rankComparison = compareRanks hand1 hand2 shouldReplaceJs
        compareHands' (c1:h1) (c2:h2)
            | null (c1:h1) && null (c2:h2) = EQ
            | c1 == c2 = compareHands' h1 h2
            | otherwise = compareCards c1 c2 cardMap

main = do
    contents <- getContents
    let ls = lines contents
        handsAndBids = map ((\[x,y] -> (x, read y :: Int)) . words) ls
        part1Map = M.fromList $ zip ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] (reverse [1..13])
        part2Map = M.fromList $ zip ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'] (reverse [1..13])
    print $ sum $ map (\(a,b) -> a * b) $ zip [1..] $ map snd $ sortBy (\(a,b) (c, d) -> compareHands a c part1Map False) handsAndBids
    print $ sum $ map (\(a,b) -> a * b) $ zip [1..] $ map snd $ sortBy (\(a,b) (c, d) -> compareHands a c part2Map True) handsAndBids
