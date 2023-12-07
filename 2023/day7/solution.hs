import qualified Data.Map as M
import Data.Char (isSpace)
import Data.List (sort)

syms = M.fromList $ zip ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] (reverse [1..13])

handKinds = M.fromList $ zip [[5,5,5,5,5], [1,4,4,4,4], [2,2,3,3,3], [1,1,3,3,3], [1,2,2,2,2], [1,1,1,2,2], [1,1,1,1,1]] (reverse [1..7])

handKind :: String -> Int
handKind xs = handKinds M.! amounts
    where amounts = sort [length $ filter (==x) xs | x <- xs]

compareHands :: String -> String -> Ordering
compareHands xs ys = compare (handKind xs) (handKind ys) <> compareSyms xs ys
  where
    compareSyms as bs
        | null as && null bs = EQ
        | sa > sb = GT
        | sa < sb = LT
        | otherwise = compareSyms (tail as) (tail bs)
        where
            sa = syms M.! head as
            sb = syms M.! head bs


data Hand = Hand {
    cards :: String,
    bid :: Int
} deriving (Show)

instance Eq Hand where
    a == b = (cards a) == (cards b)

instance Ord Hand where
    compare a b = compareHands (cards a) (cards b)


main = do
    contents <- getContents
    let ls = lines contents
        hands = sort $ map (\x -> Hand (takeWhile (not . isSpace) x) (read (dropWhile (not . isSpace) x) :: Int)) ls

    print $ foldl (\a (r, b) -> a + r*b) 0 $ zip [1..] (map bid hands)
